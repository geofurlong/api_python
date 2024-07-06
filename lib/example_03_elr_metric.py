# 1. Example of querying a single ELR which has extents reported in kilometres (i.e. a metric ELR).
# 2. Example of querying for all ELRs which have extents reported in kilometres.

# NOTE Mapping of ELR "FTC" is only valid on the limits of the British mainland.

from geofurlong import Geofurlong


gf = Geofurlong()

trl3 = gf.elr("TRL3")

print(f"ELR:              {trl3.elr}")
print(f"Route:            {trl3.route}")
print(f"Section:          {trl3.section}")
print(f"Remarks:          {trl3.remarks}")
print(f"Metric:           {trl3.metric}")
print(f"Reported Start:   {trl3.ty_from} (express as total yards)")
print(f"Reported End:     {trl3.ty_to} (express as total yards)")
print(f"Reported Extents: {trl3.formatted_range}")
print(f"Reported Length:  {trl3.reported_len_y} yards")
print(f"Reported Length:  {trl3.reported_len_km:.3f} km")
print(f"Measured Length:  {trl3.measured_len_km:.3f} km")
print(f"Grouping:         {trl3.grouping}")
print(f"Neighbours:       {trl3.neighbours}")
print(f"TRACKmap books:   {trl3.trackmaps}")

print("\nMetric ELRs")

# Loop through all known ELR codes in database.
for elr_code in gf.elr_codes:
    elr = gf.elr(elr_code)
    if elr.metric:
        print(f"{elr.elr:4} ({elr.measured_len_km:6.3f} km) : {elr.route} - {elr.section}")


"""
ELR:              TRL3
Route:            Channel Tunnel Rail Link (CTRL / HS1)
Section:          Dagenham Jn to Folkestone Eurotunnel Terminal (CTRL / ET boundary)
Remarks:          
Metric:           True
Reported Start:   22752 (express as total yards)
Reported End:     120260 (express as total yards)
Reported Extents: 20.804km - 109.966km (equivalent to 12M 1632y - 68M 0580y)
Reported Length:  97508 yards
Reported Length:  89.161 km
Measured Length:  89.155 km
Grouping:         ['TRL1', 'TRL2', 'TRL3', 'TRL5', 'TRL6', 'TRL7', 'TRL8', 'FTC']
Neighbours:       ['ACR', 'FJS1', 'FLT', 'FTC', 'HDR', 'PWS2', 'RLY', 'SBJ', 'SEV', 'TLL', 'TML', 'TRL2', 'TRL5', 'TRL6', 'TRL7', 'TRL8', 'VIR', 'XTD']
TRACKmap books:   [('5', 'Southern & TfL')]

Metric ELRs
ELL1 (10.116 km) : East London Line - near Dalston Jn to New Cross Gate Down Jn
ELL2 ( 1.454 km) : East London Line - Surrey Canal Jn to New Cross
ELL3 ( 1.453 km) : East London Line - Silwood Jn to NR / TfL interface prior to Old Kent Road Jn
ELL4 ( 0.189 km) : East London Line - NR / TfL interface to Old Kent Road Jn
FJS1 ( 6.015 km) : Waterloo Connection Line - Fawkham Jn to Southfleet Jn
FLT  ( 4.577 km) : Folkestone Eurotunnel Terminal - Cheriton Jn to Terminal to Cheriton Jn
FTC  (60.008 km) : Channel Tunnel Rail Link (CTRL / HS1) - Folkestone Eurotunnel Terminal to Calais-Coquelles Eurotunnel Terminal
HLL1 ( 6.868 km) : Heathrow Airport Link Line - Heathrow Tunnel Jn to Heathrow Airport Terminal 4
HLL2 ( 6.456 km) : Heathrow Airport Link Line - Heathrow Tunnel Jn to Heathrow Airport Terminal 5
RDO1 ( 1.342 km) : Channel Tunnel Rail Link (CTRL / HS1) - London St Pancras International to York Way South Jn
TMD1 ( 1.575 km) : Temple Mills Depot Branch - Stratford International West Jn to Temple Mills Depot
TRL1 ( 1.515 km) : Channel Tunnel Rail Link (CTRL / HS1) - London St Pancras International to York Way South Jn
TRL2 (20.800 km) : Channel Tunnel Rail Link (CTRL / HS1) - York Way South Jn to Dagenham Jn
TRL3 (89.155 km) : Channel Tunnel Rail Link (CTRL / HS1) - Dagenham Jn to Folkestone Eurotunnel Terminal (CTRL / ET boundary)
TRL5 ( 2.785 km) : Channel Tunnel Rail Link (CTRL / HS1) - North Kent Line Connection Jn to Springhead Jn
TRL6 ( 2.022 km) : Channel Tunnel Rail Link (CTRL / HS1) - Ashford West Jn to Ashford International
TRL7 ( 2.480 km) : Channel Tunnel Rail Link (CTRL / HS1) - Ashford International to Ashford East Jn
TRL8 ( 1.623 km) : Channel Tunnel Rail Link (CTRL / HS1) - Dollands Moor West Jn to Dollands Moor Yard Freight Chord
"""
