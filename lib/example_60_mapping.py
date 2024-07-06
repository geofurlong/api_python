# Example showing how to export ELR co-ordinates to GeoJSON files at varying intervals.
# NOTE requires installation of the folium library.

from geofurlong import Geofurlong
import folium


gf = Geofurlong()

wolverhampton = gf.between("RBS2", gf.ty(12, 600), gf.ty(12, 1350), lon_lat=True)

standard_map = folium.Map()

# Folium requires the co-ordinates to be in the format (latitude, longitude).
coordinates = [(y, x) for x, y in wolverhampton.coords]

folium.PolyLine(coordinates).add_to(standard_map)

standard_map.fit_bounds(standard_map.get_bounds())
standard_map.save("wolverhampton_standard.html")


satellite_map = folium.Map()

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri",
    name="Satellite",
    overlay=False,
    control=True,
).add_to(satellite_map)

folium.PolyLine(coordinates).add_to(satellite_map)
satellite_map.fit_bounds(satellite_map.get_bounds())
satellite_map.save("wolverhampton_satellite.html")
