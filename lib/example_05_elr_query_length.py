# Example of querying ELRs by their measured length.

from geofurlong import Geofurlong


gf = Geofurlong()

print("ELRs longer than 150 km\n")
print("ELR   Length     Route                                     Section")
for elr_code in gf.elr_codes:
    elr = gf.elr(elr_code)
    if elr.measured_len_km > 150.0:
        print(f"{elr.elr:4}  {elr.measured_len_km:7.3f}km  {elr.route:40}  {elr.section}")


print("\nELRs shorter than 200 metres\n")
print("ELR   Length     Route                                     Section")
for elr_code in gf.elr_codes:
    elr = gf.elr(elr_code)
    if elr.measured_len_km < 0.2:
        print(f"{elr.elr:4}  {elr.measured_len_km:7.3f}km  {elr.route:40}  {elr.section}")


"""
ELRs longer than 150 km

ELR   Length     Route                                     Section
BGK   154.668km  Bethnal Green to King's Lynn              Bethnal Green East Jn to King's Lynn
ECM1  257.803km  East Coast Main Line (ECML)               London King's Cross to Shaftholme Jn
HGL2  178.976km  Highland Main Line                        Stanley Jn to Inverness
LTN1  183.560km  Great Eastern Main Line (GEML)            London Liverpool Street to Trowse Lower Jn
MLN1  395.871km  Great Western Main Line (GWML)            London Paddington to Plymouth West
SWM2  270.052km  South Wales Main Line (SWML)              Gloucester Yard Jn to Johnston
WCK   260.044km  Far North Line                            Inverness to Wick
WHL   160.213km  West Highland Line                        Craigendoran Jn to Fort William

ELRs shorter than 200 metres

ELR   Length     Route                                     Section
AIW     0.136km  Alton Itchen Abbas and Winchester Line    
BAN1    0.151km  Baglan Branch                             Briton Ferry to Baglan Branch Jn
ELL4    0.189km  East London Line                          NR / TfL interface to Old Kent Road Jn
GGZ     0.149km  Gwaun-Cae-Gurwen Loop                     
LMD8    0.187km  London Euston                             North End Arrival and Departure Roads
MII     0.139km  Mistley Incline                           
NML     0.187km  Newport Monmouthshire Loop                
PBY     0.172km  Portbury Docks Branch                     Portbury Jn to Portbury Docks
QLT1    0.067km  Queen's Park                              LTE Lines to Up Electric Line
QLT2    0.105km  Queen's Park                              LTE Lines to Down Electric Line
RVS1    0.099km  Riverside Line                            former Clydebank Central Jn to COM
"""
