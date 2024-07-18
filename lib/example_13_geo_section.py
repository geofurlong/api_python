# Example of converting from ELR and mileage ranges to positional co-ordinates.

from geofurlong import Geofurlong


gf = Geofurlong()

elr = "WEB"
miles_from, yards_from = 91, 403
miles_to, yards_to = 92, 1274

print(
    f"Railway geographic points for ELR {elr} between {gf.format_mileage(miles_from, yards_from)} and {gf.format_mileage(miles_to, yards_to)}"
)

print("\nEasting / Northing co-ordinates")
spalding = gf.between(elr, gf.ty(miles_from, yards_from), gf.ty(miles_to, yards_to))
for location in spalding.coords:
    print(location)

print("\nLongitude / Latitude co-ordinates")
spalding_lon_lat = gf.between(elr, gf.ty(miles_from, yards_from), gf.ty(miles_to, yards_to), lon_lat=True)
for location_lon_lat in spalding_lon_lat.coords:
    print(location_lon_lat)


"""
Railway geographic points for ELR WEB between 91M 0403y and 92M 1274y

Easting / Northing co-ordinates
(523195.9951720109, 320293.8304452866)
(523612.74120000005, 321193.04289999977)
(523987.55119999964, 322000.25210000016)
(524164.6107999999, 322386.74259999953)
(524203.6831, 322471.91559999995)
(524204.86560000014, 322474.49200000055)
(524204.88939999975, 322474.5438000001)
(524206.97161044256, 322479.0804844287)

Longitude / Latitude co-ordinates
(-0.17553696992916282, 52.76620122093633)
(-0.1690247754951584, 52.77418546580441)
(-0.16316640065292187, 52.781352306787475)
(-0.1603962793053502, 52.78478421874905)
(-0.15978497212224677, 52.78554050613572)
(-0.1597664714350966, 52.78556338289829)
(-0.15976609909512965, 52.785563842842905)
(-0.15973352202137425, 52.785604125655254)
"""
