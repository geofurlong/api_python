# This script demonstrates the most basic usage of the Geofurlong Python API.


from geofurlong import Geofurlong

gf = Geofurlong()
print("GeoFurlong Python API version", gf.api_version)
print("GeoFurlong database version  ", gf.db_version)


"""
GeoFurlong Python API version 0.1.0
GeoFurlong database version   6.8.1
"""
