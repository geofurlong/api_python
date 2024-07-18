# Example of converting from ELR and mileage to positional co-ordinates.

from geofurlong import Geofurlong


gf = Geofurlong()

# Locations define a place name, ELR, mile, and yard.
locations = (
    ("Thurso", "TSO", 6, 1223),
    ("Bletchley", "LEC1", 46, 1299),
    ("Weston-super-Mare", "WSM", 137, 790),
    ("Holyhead", "CNH3", 263, 914),
    ("Lowestoft", "NOL", 23, 808),
    ("Heysham", "MHH", 4, 53),
    ("St Ives", "SIV", 325, 199),
    ("Poole", "BML2", 113, 1294),
)

print("Location             ELR    Miles  Yards  Easting      Northing      Longitude   Latitude")
print("-" * 91)

for location in locations:
    place, elr, miles, yards = location

    easting_northing = gf.at(elr, miles * Geofurlong.YARDS_IN_MILE + yards, lon_lat=False)
    longitude_latitude = gf.at(elr, miles * Geofurlong.YARDS_IN_MILE + yards, lon_lat=True)

    print(
        f"{place:<20} {elr:<5} {miles:>5}M {yards:>5}y "
        f"{easting_northing.x:>11.3f}m {easting_northing.y:>11.3f}m   "
        f"{longitude_latitude.x:>9.6f}°  {longitude_latitude.y:>9.6f}°"
    )


"""
Location             ELR    Miles  Yards  Easting      Northing      Longitude   Latitude
-------------------------------------------------------------------------------------------
Thurso               TSO       6M  1223y  311321.073m  967996.348m   -3.527216°  58.590865°
Bletchley            LEC1     46M  1299y  486832.805m  233879.131m   -0.736667°  51.996578°
Weston-super-Mare    WSM     137M   790y  332385.296m  161033.988m   -2.972161°  51.344350°
Holyhead             CNH3    263M   914y  224761.827m  382113.156m   -4.631527°  53.306890°
Lowestoft            NOL      23M   808y  654666.231m  292874.232m    1.748509°  52.474332°
Heysham              MHH       4M    53y  340277.313m  460084.122m   -2.913311°  54.033268°
St Ives              SIV     325M   199y  151978.173m   40087.421m   -5.477450°  50.208700°
Poole                BML2    113M  1294y  401259.558m   91000.557m   -1.983522°  50.718631°
"""
