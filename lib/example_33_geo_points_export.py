# Example showing how to export ELR co-ordinates to GeoJSON files at varying intervals.
# NOTE requires installation of the geopandas library.

import os
import geopandas as gpd
from shapely.geometry import Point
from geofurlong import Geofurlong


gf = Geofurlong()

intervals = (440, 880, 1_760, 1_760 * 5, 1_760 * 10)

groups = (
    ("East Coast Main Line (South)", "ecml-s", ("ECM1", "ECM2", "ECM3", "ECM4", "ECM5", "ECM6", "ECM7", "ECM8", "ECM9")),
    ("Midland Main Line", "mml", ("SPC1", "SPC2", "SPC3", "SPC4", "SPC5", "SPC6", "SPC7", "SPC8", "SPC9")),
    ("East Coast Main Line (North)", "ecml-n", ("ECN1", "ECN2", "ECN3", "ECN4", "ECN5")),
    ("Scottish Central Main Line", "scm", ("SCM1", "SCM2", "SCM3", "SCM4", "SCM5")),
    ("Glasgow-Ayr Line", "ayr", ("AYR1", "AYR2", "AYR3", "AYR4", "AYR5", "AYR6")),
    ("Cumbrian Coast Line", "cumbria", ("CBC1", "CBC2", "CBC3")),
    ("Edinburgh-Carstairs Line", "ed-car", ("ECA1", "ECA2", "ECA3")),
    ("Pye Bridge-Shirebrook Line", "pbs", ("PBS1", "PBS2", "PBS3")),
    ("Windsor Bridge-Southport Line", "wbs", ("WBS1", "WBS2", "WBS3")),
    ("Aberdeen-Inverness Line", "ani", ("ANI1", "ANI2", "ANI3")),
    ("North London Line", "nll", ("BOK1", "BOK2", "BOK3", "BOK4", "BOK5", "BOK6")),
    ("Edinburgh-Glasgow Main Line", "egm", ("EGM1", "EGM2", "EGM3", "EGM4")),
    ("Millerhill", "mhl", ("MHL1", "MHL2", "MHL3", "MHL4")),
    ("Borders", "borders", ("NNS", "SBO")),
    ("Channel Tunnel Rail Link (HS1)", "ctrl", ("TRL1", "TRL2", "TRL3", "TRL5", "TRL6", "TRL7", "TRL8")),
    (
        "West Coast Main Line",
        "wcml",
        ("LEC1", "LEC2", "LEC3", "LEC4", "LEC5", "LEC6", "CGJ1", "CGJ2", "CGJ3", "CGJ4", "CGJ5", "CGJ6", "CGJ7", "WCM1", "WCM2"),
    ),
    ("FTC", "ftc", ("FTC",)),
)


output_dir = "output/elr"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for group in groups:
    description, filename, elrs = group
    print(description)

    for interval in intervals:
        geojson_fn = f"{output_dir}/{interval:05d}/{filename}_{interval:05d}.geojson"
        if os.path.exists(geojson_fn):
            continue

        data = []

        for elr in elrs:
            metric = gf.elr(elr).metric

            for total_yards in gf.traverse(elr, interval):
                location = gf.at(elr, total_yards, lon_lat=True)
                mileage = gf.format_linear(total_yards, metric)
                data.append(
                    {"geometry": Point(location.x, location.y), "elr": elr, "mileage": mileage, "elr_mileage": f"{elr} {mileage}"}
                )

        gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
        gdf.to_file(geojson_fn, driver="GeoJSON")
