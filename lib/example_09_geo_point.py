# Example of converting from ELR and mileage to positional co-ordinates.

from geofurlong import Geofurlong


gf = Geofurlong()

print("Co-ordinates of ELR TSO at 6M 1223y (Thurso)")
thurso_easting_northing = gf.at("TSO", 6 * 1760 + 1223)
print("Ordnance Survey Easting/Northing:", thurso_easting_northing.x, thurso_easting_northing.y)

thurso_lon_lat = gf.at("TSO", 6 * 1760 + 1223, lon_lat=True)
print("Longitude/Latitude:              ", thurso_lon_lat.x, thurso_lon_lat.y)


print("\nCo-ordinates of ELR LEC1 at 46M 1299y (Bletchley)")
# Use helper function to build total yards.
bletchley_easting_northing = gf.at("LEC1", gf.build_total_yards(46, 1299))
print(f"Ordnance Survey Easting/Northing: {bletchley_easting_northing.x:.3f}m, {bletchley_easting_northing.y:.3f}m")

bletchley_lon_lat = gf.at("LEC1", gf.build_total_yards(46, 1299), lon_lat=True)
print(f"Longitude/Latitude:               {bletchley_lon_lat.x:.6f}°, {bletchley_lon_lat.y:.6f}°")


# Use shorter helper function gf.ty (instead of more verbose gf.build_total_yards) to build total yards.
print("\nCo-ordinates of ELR WSM at 137M 0790y (Weston-super-Mare)")
wsm_e_n = gf.at("WSM", gf.ty(137, 790), lon_lat=False)
print(f"Ordnance Survey Easting/Northing: {wsm_e_n.x:.3f}m, {wsm_e_n.y:.3f}m")

wsm_lon_lat = gf.at("WSM", gf.ty(137, 790), lon_lat=True)
print(f"Longitude/Latitude:               {wsm_lon_lat.x:.6f}°, {wsm_lon_lat.y:.6f}°")


"""
Co-ordinates of ELR TSO at 6M 1223y (Thurso)
Ordnance Survey Easting/Northing: 311321.0733000003 967996.3483000007
Longitude/Latitude:               -3.5272155802266454 58.590865068348485

Co-ordinates of ELR LEC1 at 46M 1299y (Bletchley)
Ordnance Survey Easting/Northing: 486832.805m, 233879.131m
Longitude/Latitude:               -0.736667°, 51.996578°

Co-ordinates of ELR WSM at 137M 0790y (Weston-super-Mare)
Ordnance Survey Easting/Northing: 332385.296m, 161033.988m
Longitude/Latitude:               -2.972161°, 51.344350°
"""
