# GeoFurlong Python API
# https://www.geofurlong.com/
# https://www.github.com/geofurlong


from typing import List, Tuple, Optional, Iterator
from dataclasses import dataclass
import sqlite3
import re
import numpy as np
import shapely.wkb
from shapely.ops import substring, transform
from shapely import offset_curve
from pyproj import CRS, Transformer


@dataclass
class ELR_Attributes:
    """Represents the key attributes, geometry, and linear calibration of an ELR."""

    # ELR code.
    elr: str = None

    # Reported low mileage limit of ELR (as total yards).
    ty_from: float = None

    # Reported high mileage limit of ELR (as total yards).
    ty_to: float = None

    # Metric (kilometres) or imperial (mileage) reporting units.
    metric: bool = None

    # Formatted mileage or kilometreage range of ELR.
    formatted_range: str = None

    # Reported length of ELR (yards).
    reported_len_y: int = None

    # Reported length of ELR (kilometres).
    reported_len_km: float = None

    # Measured length of ELR (kilometres).
    measured_len_km: float = None

    # Route description of ELR.
    route: str = None

    # Section description of ELR.
    section: str = None

    # Remarks about ELR.
    remarks: str = None

    # Grouping of ELR.
    grouping: List[str] = None

    # Neighbouring ELRs.
    neighbours: List[str] = None

    # TRACKmap(s) ELR is located within (AKA Quail Maps).
    trackmaps: List[Tuple[str, str]] = None

    # Virtual centre-line geometry of ELR.
    geometry: shapely.geometry.LineString = None

    # Linear calibration data for ELR.
    calibration: np.ndarray = None


class Geofurlong:
    """Geofurlong API for accessing railway geospatial and attribute data."""

    # Python API version.
    API_VERSION = "0.1.0"

    # Number of yards in a mile.
    YARDS_IN_MILE = 1_760

    # Number of yards in a chain.
    YARDS_IN_CHAIN = 22

    # Number of kilometres in a mile.
    KM_IN_MILE = 1.609344

    # Number of kilometres in a yard.
    KM_IN_YARD = 0.0009144

    # Regular expression to validate ELR codes.
    ELR_RegExp = re.compile(r"^[A-Z]{3}\d?$")

    def __init__(self, db_fn: str = "geofurlong.sqlite"):
        """API constructor."""

        # Open the SQLite database in read-only mode.
        self._geo_db = sqlite3.connect(f"file:{db_fn}?mode=ro", uri=True)

        # ~10 MB SQLite database cache size.
        self._geo_db.execute("PRAGMA cache_size = -10000")

        # Transform the co-ordinate system from EPSG:27700 (Planar) to EPSG:4326 (Geographic).
        self._transformer = Transformer.from_crs(CRS("EPSG:27700"), CRS("EPSG:4326"), always_xy=True)

        # Load all the ELR codes from the database.
        self._load_all_elr_codes()

        # Set up dictionary to act as cache for ELR attributes.
        self._elr_cache = {}

        # The attributes of the currently loaded ELR.
        self._elr_attrs = ELR_Attributes()

    @property
    @staticmethod
    def api_version(self) -> str:
        """Return the version of the Python API."""

        return Geofurlong.API_VERSION

    @property
    def db_version(self) -> str:
        """Return the version of the SQLite database."""

        cursor = self._geo_db.cursor()
        cursor.execute("SELECT value FROM version WHERE property='version'")
        return cursor.fetchone()[0]

    def _load_all_elr_codes(self):
        """Loads all ELR codes from the database."""

        cursor = self._geo_db.cursor()
        cursor.execute("SELECT elr FROM elr ORDER BY elr")
        self.elr_codes = tuple(row[0] for row in cursor.fetchall())

    @property
    def properties(self) -> ELR_Attributes:
        """Returns the attributes and geometry of the current ELR."""

        if self._elr_attrs is None:
            return None
        return ELR_Attributes(
            elr=self._elr_attrs.elr,
            ty_from=self._elr_attrs.ty_from,
            ty_to=self._elr_attrs.ty_to,
            reported_len_y=self._elr_attrs.ty_to - self._elr_attrs.ty_from,
            reported_len_km=(self._elr_attrs.ty_to - self._elr_attrs.ty_from) / Geofurlong.YARDS_IN_MILE * Geofurlong.KM_IN_MILE,
            metric=self._elr_attrs.metric,
            measured_len_km=self._elr_attrs.measured_len_km,
            formatted_range=self._elr_attrs.formatted_range,
            route=self._elr_attrs.route,
            section=self._elr_attrs.section,
            remarks=self._elr_attrs.remarks,
            trackmaps=self._elr_attrs.trackmaps,
            grouping=self._elr_attrs.grouping,
            neighbours=self._elr_attrs.neighbours,
            geometry=self._elr_attrs.geometry,
            # NOTE calibration is not included.
        )

    def elr(self, elr: str) -> ELR_Attributes:
        """Load the attributes, centre-line geometry, and calibration of the ELR."""

        if elr == self._elr_attrs.elr:
            # ELR is already loaded.
            return self.properties

        if elr in self._elr_cache:
            # ELR is cached.
            self._elr_attrs = self._elr_cache[elr]
            return self.properties

        # Check ELR code is valid.
        if not Geofurlong.valid_elr(elr):
            raise ValueError(f"Invalid ELR code: {elr}")

        # Load ELR from database.
        sql_elr = "SELECT total_yards_from, total_yards_to, l_system, shape_length_m, geometry, route, section, remarks, grouping, neighbours, quail_book FROM elr WHERE elr=? LIMIT 1"
        cursor_elr = self._geo_db.execute(sql_elr, (elr,))
        row_elr = cursor_elr.fetchone()
        if not row_elr:
            raise ValueError(f"ELR not known: {elr}")

        elr_ty_from_index, elr_ty_to_index, elr_metric_index, elr_shape_len_m = 0, 1, 2, 3
        elr_geometry_index = 4
        route_index, section_index, remarks_index = 5, 6, 7
        grouping_index, neighbours_index, trackmaps_index = 8, 9, 10

        ty_from = int(row_elr[elr_ty_from_index])
        ty_to = int(row_elr[elr_ty_to_index])
        metric = row_elr[elr_metric_index] == "K"

        fm, fy = Geofurlong.split_total_yards(ty_from)
        tm, ty = Geofurlong.split_total_yards(ty_to)

        if metric:
            fkm = ty_from / Geofurlong.YARDS_IN_MILE * Geofurlong.KM_IN_MILE
            tkm = ty_to / Geofurlong.YARDS_IN_MILE * Geofurlong.KM_IN_MILE
            formatted_range = f"{fkm:.3f}km - {tkm:.3f}km (equivalent to {Geofurlong.mileage_verbose(fm, fy, tm, ty)})"
        else:
            formatted_range = Geofurlong.mileage_verbose(fm, fy, tm, ty)

        trackmaps = [(book, Geofurlong.trackmap_coverage(book)) for book in row_elr[trackmaps_index].split(";")]

        attrs = ELR_Attributes(
            elr=elr,
            ty_from=ty_from,
            ty_to=ty_to,
            metric=metric,
            formatted_range=formatted_range,
            measured_len_km=row_elr[elr_shape_len_m] / 1_000,
            route=row_elr[route_index],
            section=row_elr[section_index],
            remarks=row_elr[remarks_index],
            trackmaps=trackmaps,
            grouping=row_elr[grouping_index].split(";"),
            neighbours=row_elr[neighbours_index].split(";"),
            geometry=shapely.wkb.loads(row_elr[elr_geometry_index]),
            calibration=np.empty(0),
        )

        # Load the ELR calibration data (sorted by mileage / kilometreage) into a numpy array.
        sql_calibration = (
            "SELECT total_yards_from, total_yards_to, linear_offset_from_m, linear_offset_to_m "
            "FROM calibration WHERE elr=? "
            "ORDER BY total_yards_from"
        )

        cursor_calibration = self._geo_db.execute(sql_calibration, (elr,))
        rows_calibration = cursor_calibration.fetchall()

        if len(rows_calibration) == 0:
            raise ValueError(f"No calibration data for {elr}")

        attrs.calibration = np.array(
            rows_calibration,
            dtype=[
                ("ty_from", np.int32),
                ("ty_to", np.int32),
                ("lo_from", np.float32),
                ("lo_to", np.float32),
            ],
        )

        self._elr_cache[elr] = attrs  # Add to cache.
        self._elr_attrs = attrs  # Set "current" ELR.
        return self.properties

    def _linear_offset(self, ty: int) -> float:
        """Returns the linear offset of a mileage point (expressed as total yards) of the current ELR."""

        # Binary search for the calibration segment containing the total yards.
        idx = np.searchsorted(self._elr_attrs.calibration["ty_from"], ty, side="right") - 1

        if idx < 0 or ty > self._elr_attrs.calibration["ty_to"][idx]:
            m, y = Geofurlong.split_total_yards(ty)
            elr_range = self._elr_attrs.formatted_range
            raise ValueError(f"No calibration data for {self._elr_attrs.elr} segment {Geofurlong.fmt(m, y)}: {elr_range}")

        ty_from = self._elr_attrs.calibration["ty_from"][idx]
        ty_to = self._elr_attrs.calibration["ty_to"][idx]
        lo_from = self._elr_attrs.calibration["lo_from"][idx]
        lo_to = self._elr_attrs.calibration["lo_to"][idx]
        linear_offset = lo_from + ((ty - ty_from) / (ty_to - ty_from) * (lo_to - lo_from))

        return linear_offset

    def _validate_elr_mileage(self, elr: str, ty: int) -> None:
        """Checks that the requested mileage is within the ELR limits."""

        # Check ELR code is valid/available and miles/yards are valid.
        self.elr(elr)

        # Check the requested mileage is within the ELR limits.
        if (ty < self._elr_attrs.ty_from) or (ty > self._elr_attrs.ty_to):
            ty_mileage = Geofurlong.format_total_yards(ty)
            elr_start = Geofurlong.format_total_yards(self._elr_attrs.ty_from)
            elr_end = Geofurlong.format_total_yards(self._elr_attrs.ty_to)

            raise ValueError(
                f"Mileage of {ty_mileage} [{ty}] on ELR {self._elr_attrs.elr} outwith valid bounds: {elr_start} [{self._elr_attrs.ty_from}] - {elr_end} [{self._elr_attrs.ty_to}]"
            )

    def at(self, elr: str, ty: int, lon_lat: bool = False) -> Optional[shapely.geometry.Point]:
        """Returns the point geometry of a mileage point on an ELR."""

        self._validate_elr_mileage(elr, ty)
        lo = self._linear_offset(ty)
        point_geometry = self._elr_attrs.geometry.interpolate(lo)

        if lon_lat:
            # Transform geometry from Planar to Geographic.
            return transform(self._transformer.transform, point_geometry)

        return point_geometry

    def between(self, elr: str, ty_from, ty_to: int, lon_lat: bool = False) -> Optional[shapely.geometry.LineString]:
        """Returns a portion of the ELR geometry between two mileage points."""

        if ty_to < ty_from:
            ty_from, ty_to = ty_to, ty_from

        self._validate_elr_mileage(elr, ty_from)
        self._validate_elr_mileage(elr, ty_to)

        lo_from = self._linear_offset(ty_from)
        lo_to = self._linear_offset(ty_to)

        substring_geometry = substring(self._elr_attrs.geometry, lo_from, lo_to)

        if lon_lat:
            return transform(self._transformer.transform, substring_geometry)

        return substring_geometry

    def traverse(self, elr: str, interval: int = 1760) -> Iterator[int]:
        """
        Generates an iterator yielding total track yards at the specified interval within the ELR.
        It always includes the start and end of the ELR, irrespective of the specified interval.
        """

        if not isinstance(interval, int) or interval <= 0:
            raise TypeError("interval must be a positive integer above zero")

        elr_attrs = self.elr(elr)
        ty_from = elr_attrs.ty_from
        ty_to = elr_attrs.ty_to

        for i in range(ty_from, ty_to + 1):
            if i == ty_from or i == ty_to or i % interval == 0:
                yield i

    @staticmethod
    def valid_elr(elr: str) -> bool:
        """Checks if an ELR code is valid."""

        return Geofurlong.ELR_RegExp.match(elr) is not None

    @staticmethod
    def valid_mile(mile: int) -> bool:
        """Checks if a mile value is valid."""

        return 0 <= mile < 350

    @staticmethod
    def valid_yard(yard: int) -> bool:
        """Checks if a yard value is valid."""

        return -1759 <= yard < 1760

    @staticmethod
    def miles_yards_to_total_yards(miles_yards: float) -> int:
        """Convert a floating-point decimal mileage (of form mmm.yyyy) to a total yards integer."""

        miles = int(miles_yards)
        return int(round(Geofurlong.YARDS_IN_MILE * miles + 10_000 * (miles_yards - miles), 0))

    @staticmethod
    # TODO add equivalent functionality for metric ELRs.
    def build_total_yards(miles: int, yards: int) -> int:
        """Builds a total yards integer from component miles and yards integers."""

        if not Geofurlong.valid_mile(miles) or not Geofurlong.valid_yard(yards):
            raise ValueError(f"Invalid mileage: {miles}M {yards}y")

        return miles * Geofurlong.YARDS_IN_MILE + yards

    @staticmethod
    def ty(miles: int, yards: int) -> int:
        """Alias for `build_total_yards` method."""

        return Geofurlong.build_total_yards(miles, yards)

    @staticmethod
    def split_total_yards(total_yards: int) -> tuple[int, int]:
        """Splits a total yards integer into component miles and yards integers."""

        if total_yards >= 0:
            miles = int(total_yards / Geofurlong.YARDS_IN_MILE)
            yards = total_yards % Geofurlong.YARDS_IN_MILE
            return (miles, yards)
        return (0, total_yards)

    @staticmethod
    def mileage_verbose(fm, fy, tm, ty: int) -> str:
        """Returns a string representation of a mileage range."""

        if (fm == tm) and (fy == ty):
            return f"{fm}M {fy:04}y"
        return f"{fm}M {fy:04}y - {tm}M {ty:04}y"

    @staticmethod
    def km_verbose(fkm, fm, tkm, tm: int) -> str:
        """Returns a string representation of a kilometreage range."""

        if (fkm == tkm) and (fm == tm):
            return f"{fkm}.{fm:03}km"
        return f"{fkm}.{fm:03}km - {tkm}.{tm:03}km"

    @staticmethod
    def format_mileage(miles: int, yards: int) -> str:
        """Converts component miles and yards into a combined formatted string."""

        return f"{miles}M {int(yards):04d}y"

    @staticmethod
    def fmt(miles: int, yards: int) -> int:
        """Alias for `format_mileage` method."""

        return Geofurlong.format_mileage(miles, yards)

    @staticmethod
    def format_total_yards(total_yards: int) -> str:
        """Converts a total yards number as a formatted string."""

        m, y = Geofurlong.split_total_yards(total_yards)
        return Geofurlong.format_mileage(m, y)

    @staticmethod
    def total_yards_to_km(total_yards: int) -> tuple[int, int]:
        """Converts a total yards number to componenent kilometre and metre parts."""

        km = round(total_yards * Geofurlong.KM_IN_YARD, 3)
        m = int((km - int(km)) * 1_000)
        km = int(km)
        return km, m

    @staticmethod
    def format_linear(total_yards: int, metric: bool) -> str:
        """Converts a total yards number to a formatted string utilising the reported units"""

        if metric:
            km, m = Geofurlong.total_yards_to_km(total_yards)
            return Geofurlong.km_verbose(km, m, km, m)
        else:
            return Geofurlong.format_total_yards(total_yards)

    @staticmethod
    def trackmap_coverage(book: str) -> str:
        """Returns the coverage area description of a TRACKmaps (Quail) book."""

        book = int(book)

        # The TRACKmaps books are effectively fixed, thus hard-coded below.
        coverage = {
            1: "Scotland",
            2: "Eastern",
            3: "Western & Wales",
            4: "Midlands & North West",
            5: "Southern & TfL",
        }

        if book not in coverage:
            raise ValueError(f"Book {book} not found in coverage")

        return coverage[book]
