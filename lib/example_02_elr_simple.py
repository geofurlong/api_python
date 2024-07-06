# Example of querying a single ELR on a branch line.

from geofurlong import Geofurlong


gf = Geofurlong()

nbk = gf.elr("NBK")

print(f"ELR:              {nbk.elr}")
print(f"Route:            {nbk.route}")
print(f"Section:          {nbk.section}")
print(f"Remarks:          {nbk.remarks}")
print(f"Metric:           {nbk.metric}")
print(f"Reported Start:   {nbk.ty_from} (express as total yards)")
print(f"Reported End:     {nbk.ty_to} (express as total yards)")
print(f"Reported Extents: {nbk.formatted_range}")
print(f"Reported Length:  {nbk.reported_len_y} yards")
print(f"Reported Length:  {nbk.reported_len_km:.3f} km")
print(f"Measured Length:  {nbk.measured_len_km:.3f} km")
print(f"Grouping:         {nbk.grouping}")
print(f"Neighbours:       {nbk.neighbours}")
print(f"TRACKmap book(s): {nbk.trackmaps}")


"""
ELR:              NBK
Route:            North Berwick Branch
Section:          Drem Jn to North Berwick
Remarks:          
Metric:           False
Reported Start:   31868 (express as total yards)
Reported End:     39355 (express as total yards)
Reported Extents: 18M 0188y - 22M 0635y
Reported Length:  7487 yards
Reported Length:  6.846 km
Measured Length:  6.787 km
Grouping:         ['']
Neighbours:       ['ECM8']
TRACKmap book(s): [('1', 'Scotland')]
"""
