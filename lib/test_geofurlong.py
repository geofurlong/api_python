# GeoFurlong unit tests.

import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from shapely.geometry import LineString, Point
from geofurlong import Geofurlong, ELR_Attributes


@pytest.mark.parametrize(
    "mile, expected",
    [
        (0, True),
        (100, True),
        (349, True),
        (-1, False),
        (350, False),
        (400, False),
    ],
)
def test_valid_mile(mile, expected):
    assert Geofurlong.valid_mile(mile) == expected


@pytest.mark.parametrize(
    "yard, expected",
    [
        (-1759, True),
        (0, True),
        (1, True),
        (1759, True),
        (-1760, False),
        (1760, False),
    ],
)
def test_valid_yard(yard, expected):
    assert Geofurlong.valid_yard(yard) == expected


@pytest.mark.parametrize(
    "elr, expected",
    [
        ("ECM8", True),
        ("LTN1", True),
        ("SOY", True),
        ("", False),
        ("ecm8", False),
        ("Ecm8", False),
        ("ECm8", False),
        ("ECM 8", False),
        (" ECM8", False),
        ("", False),
        ("ECM88", False),
        ("1234", False),
        ("8ECM", False),
    ],
)
def test_valid_elr(elr, expected):
    assert Geofurlong.valid_elr(elr) == expected


@pytest.mark.parametrize(
    "miles_yards, expected",
    [
        (-0.0001, -1),
        (0.0, 0),
        (0.0001, 1),
        (0.001, 10),
        (0.01, 100),
        (0.1, 1_000),
        (0.1759, 1_759),
        (1.0, 1_760),
        (9.1759, 17_599),
        (10.0, 17_600),
        (100.0, 176_000),
        (100.0001, 176_001),
    ],
)
def test_miles_yards_to_total_yards(miles_yards, expected):
    assert Geofurlong.miles_yards_to_total_yards(miles_yards) == expected


@pytest.mark.parametrize(
    "miles, yards, expected",
    [
        (0, -1, -1),
        (0, 0, 0),
        (0, 1, 1),
        (0, 10, 10),
        (0, 100, 100),
        (0, 1_000, 1_000),
        (0, 1_759, 1_759),
        (1, 0, 1_760),
        (1, 9, 1_769),
        (10, 0, 17_600),
        (100, 0, 176_000),
        (100, 999, 176_999),
    ],
)
def test_build_total_yards(miles, yards, expected):
    assert Geofurlong.build_total_yards(miles, yards) == expected


@pytest.mark.parametrize(
    "total_yards, expected",
    [
        (-1, (0, -1)),
        (0, (0, 0)),
        (1, (0, 1)),
        (10, (0, 10)),
        (100, (0, 100)),
        (1_000, (0, 1_000)),
        (1_759, (0, 1_759)),
        (1_760, (1, 0)),
        (1_769, (1, 9)),
        (17_600, (10, 0)),
        (176_000, (100, 0)),
        (176_999, (100, 999)),
    ],
)
def test_explode_total_yards(total_yards, expected):
    assert Geofurlong.split_total_yards(total_yards) == expected


@pytest.mark.parametrize(
    "fm, fy, tm, ty, expected",
    [
        (0, 0, 0, 0, "0M 0000y"),
        (0, 0, 0, 1, "0M 0000y - 0M 0001y"),
        (9, 1759, 10, 1, "9M 1759y - 10M 0001y"),
        (78, 324, 194, 1098, "78M 0324y - 194M 1098y"),
    ],
)
def test_mileage_verbose(fm, fy, tm, ty, expected):
    assert Geofurlong.mileage_verbose(fm, fy, tm, ty) == expected


@pytest.mark.parametrize(
    "fkm, fm, tkm, tm, expected",
    [
        (0, 0, 0, 0, "0.000km"),
        (0, 0, 0, 1, "0.000km - 0.001km"),
        (13, 998, 15, 4, "13.998km - 15.004km"),
        (123, 47, 124, 56, "123.047km - 124.056km"),
    ],
)
def test_km_verbose(fkm, fm, tkm, tm, expected):
    assert Geofurlong.km_verbose(fkm, fm, tkm, tm) == expected


@pytest.mark.parametrize(
    "miles, yards, expected",
    [
        (0, 0, "0M 0000y"),
        (0, 1, "0M 0001y"),
        (9, 1759, "9M 1759y"),
        (194, 1098, "194M 1098y"),
    ],
)
def test_format_mileage(miles, yards, expected):
    assert Geofurlong.format_mileage(miles, yards) == expected


@pytest.mark.parametrize(
    "total_yards, expected",
    [
        (0, "0M 0000y"),
        (1, "0M 0001y"),
        (1_760, "1M 0000y"),
        (17_601, "10M 0001y"),
    ],
)
def test_format_total_yards(total_yards, expected):
    assert Geofurlong.format_total_yards(total_yards) == expected


@pytest.mark.parametrize(
    "total_yards, expected",
    [
        (0, (0, 0)),
        (1, (0, 1)),
        (1_000, (0, 914)),
        (1_094, (1, 0)),
        (10_000, (9, 144)),
    ],
)
def test_total_yards_to_km(total_yards, expected):
    assert Geofurlong.total_yards_to_km(total_yards) == expected


@pytest.mark.parametrize(
    "total_yards, metric, expected",
    [
        (0, False, "0M 0000y"),
        (1, False, "0M 0001y"),
        (1_000, False, "0M 1000y"),
        (1_760, False, "1M 0000y"),
        (17_600, False, "10M 0000y"),
        (0, True, "0.000km"),
        (1, True, "0.001km"),
        (1_000, True, "0.914km"),
        (1_094, True, "1.000km"),
        (10_000, True, "9.144km"),
    ],
)
def test_format_linear(total_yards, metric, expected):
    assert Geofurlong.format_linear(total_yards, metric) == expected


@pytest.mark.parametrize(
    "book, expected, expected_exception, expected_message",
    [
        ("2", "Eastern", None, None),
        ("3", "Western & Wales", None, None),
        ("9", None, ValueError, "Book 9 not found in coverage"),
    ],
)
def test_trackmap_coverage(book, expected, expected_exception, expected_message):
    if expected_exception:
        with pytest.raises(expected_exception, match=expected_message):
            Geofurlong.trackmap_coverage(book)
    else:
        assert Geofurlong.trackmap_coverage(book) == expected


def test_linear_offset():
    gf = Geofurlong()

    calibration = np.array(
        [(0, 1_000, 50.0, 80.0), (1_000, 11_000, 80.0, 180.0)],
        dtype=[
            ("ty_from", np.int32),
            ("ty_to", np.int32),
            ("lo_from", np.float32),
            ("lo_to", np.float32),
        ],
    )

    gf._elr_attrs = ELR_Attributes(calibration=calibration)

    assert gf._linear_offset(0) == 50.0
    assert gf._linear_offset(500) == 65.0
    assert gf._linear_offset(1_000) == 80.0
    assert gf._linear_offset(6_000) == 130.0
    assert gf._linear_offset(11_000) == 180.0

    with pytest.raises(ValueError):
        gf._linear_offset(-999)

    with pytest.raises(ValueError):
        gf._linear_offset(99_999)


@pytest.fixture
def mock_geofurlong():
    gf = Geofurlong()
    # Mock the elr method to not perform any database operations.
    gf.elr = MagicMock(return_value=None)
    gf._elr_attrs = MagicMock()
    gf._elr_attrs.elr = "TEST"
    gf._elr_attrs.ty_from = -123
    gf._elr_attrs.ty_to = 9_999
    return gf


def test_validate_elr_mileage_valid(mock_geofurlong):
    mock_geofurlong._validate_elr_mileage("TEST", -123)
    mock_geofurlong._validate_elr_mileage("TEST", 0)
    mock_geofurlong._validate_elr_mileage("TEST", 9_999)


def test_validate_elr_mileage_invalid(mock_geofurlong):
    with pytest.raises(ValueError) as excinfo:
        mock_geofurlong._validate_elr_mileage("TEST", -124)
    assert "outwith valid bounds" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        mock_geofurlong._validate_elr_mileage("TEST", 10_000)
    assert "outwith valid bounds" in str(excinfo.value)


@pytest.fixture
def geofurlong_instance():
    return Geofurlong()


@patch("geofurlong.Geofurlong._validate_elr_mileage")
@patch("geofurlong.Geofurlong._linear_offset", return_value=100)
def test_at(mock_linear_offset, mock_validate_elr_mileage, geofurlong_instance):
    test_linestring = LineString([(100, 500), (400, 900)])

    geofurlong_instance._elr_attrs = MagicMock()
    geofurlong_instance._elr_attrs.geometry = test_linestring

    point_geometry = geofurlong_instance.at("TEST", 0)
    assert isinstance(point_geometry, Point)
    assert point_geometry.x == 160 and point_geometry.y == 580


@patch("geofurlong.Geofurlong._validate_elr_mileage")
@patch("geofurlong.Geofurlong._linear_offset")
def test_between(mock_linear_offset, mock_validate_elr_mileage, geofurlong_instance):
    test_linestring = LineString([(100, 500), (400, 900)])

    mock_linear_offset.side_effect = [100, 500]

    geofurlong_instance._elr_attrs = MagicMock()
    geofurlong_instance._elr_attrs.geometry = test_linestring

    linestring_geometry = geofurlong_instance.between("TEST", 0, 1000, lon_lat=False)
    assert isinstance(linestring_geometry, LineString)
    expected_linestring = LineString([(160, 580), (400, 900)])
    assert linestring_geometry.equals(expected_linestring)


def test_traverse(geofurlong_instance):
    elr = "TEST"
    ty_from = -123
    ty_to = 1501
    interval = 500

    mock_elr_attrs = MagicMock()
    mock_elr_attrs.ty_from = ty_from
    mock_elr_attrs.ty_to = ty_to
    geofurlong_instance.elr = MagicMock(return_value=mock_elr_attrs)

    expected_yards = [-123, 0, 500, 1000, 1500, 1501]
    generated_yards = list(geofurlong_instance.traverse(elr, interval))

    assert generated_yards == expected_yards
