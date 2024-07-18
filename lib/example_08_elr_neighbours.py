# Example of querying neighbours of ELRs.

from geofurlong import Geofurlong


gf = Geofurlong()


def view_neighbours(elr: str) -> None:
    target_elr = gf.elr(elr)
    neighbours = target_elr.neighbours

    print("ELR:              ", target_elr.elr)
    print("Route:            ", target_elr.route)
    print("Section:          ", target_elr.section)
    print("Neighbouring ELRs:", neighbours)
    print("Neighbour count:  ", len(neighbours))

    for i, neighbour in enumerate(neighbours, start=1):
        neighbour_elr = gf.elr(neighbour)
        print(f"{i:2}  {neighbour_elr.elr:4}  {neighbour_elr.route} - {neighbour_elr.section}")


if __name__ == "__main__":
    target_elrs = ("TSO", "SOY", "PLO", "BSW", "BSP1", "SPC8")
    for target_elr in target_elrs:
        view_neighbours(target_elr)
        print()


"""
ELR:               TSO
Route:             Thurso Branch (Far North Line)
Section:           Georgemas Jn to Thurso
Neighbouring ELRs: ['WCK']
Neighbour count:   1
 1  WCK   Far North Line - Inverness to Wick

ELR:               SOY
Route:             Northam Jn to Southampton Eastern Docks
Section:           
Neighbouring ELRs: ['BML1', 'BML2']
Neighbour count:   2
 1  BML1  London Waterloo to Weymouth - London Waterloo to Northam Jn
 2  BML2  London Waterloo to Weymouth - Northam Jn to Dorchester Jn

ELR:               PLO
Route:             Plymouth Loop No. 1
Section:           Lipson Jn to Speedway Jn
Neighbouring ELRs: ['FRY', 'LAS', 'MLN1', 'SUT1', 'SUT2']
Neighbour count:   5
 1  FRY   Friary Branch - former Friary Jn to Plymouth Friary
 2  LAS   Laira Sidings - 
 3  MLN1  Great Western Main Line (GWML) - London Paddington to Plymouth West
 4  SUT1  Sutton Harbour Branch (Plymouth) - Laira Jn to Mount Gold Jn
 5  SUT2  Sutton Harbour Branch (Plymouth) - Mount Gold Jn to former Friary Jn

ELR:               BSW
Route:             Bristol and South Wales Union Line
Section:           Bristol East Jn to Severn Tunnel Jn
Neighbouring ELRs: ['AFR', 'BAW', 'BLL', 'CNX', 'CWT', 'FEC', 'FWC', 'MLN1', 'PAC', 'SBK1', 'SBK2', 'SWB', 'SWM2']
Neighbour count:   13
 1  AFR   Avonmouth and Filton Line - Stoke Gifford Jn to Bristol Bulk Handling Terminal
 2  BAW   Bristol to Avonside Wharf - Easton Road Jn to Barrow Road Refuse Depot
 3  BLL   Bristol Loop Line - Feeder Bridge Jn to Dr Day’s Jn
 4  CNX   Clifton and Avonmouth Line - Narroways Hill Jn to St Andrew’s Jn
 5  CWT   Caerwent Branch - Caerwent Branch Jn to RAF Caerwent
 6  FEC   Filton East Curve - Stoke Gifford No. 1 Jn to Filton No. 1 Jn
 7  FWC   Filton West Curve - Filton No. 2 Jn to Filton West No. 2 Jn
 8  MLN1  Great Western Main Line (GWML) - London Paddington to Plymouth West
 9  PAC   Patchway Curve - Patchway No. 1 Jn to Filton West No. 1 Jn
10  SBK1  Sudbrook Branch - Caldicot to COM
11  SBK2  Sudbrook Branch - COM to Sudbrook
12  SWB   South Wales and Bristol Direct Line - Wootton Bassett Jn to Patchway No. 2 Jn
13  SWM2  South Wales Main Line (SWML) - Gloucester Yard Jn to Johnston

ELR:               BSP1
Route:             Battersea Pier Jn to Pouparts Jn
Section:           Battersea Pier Jn to Longhedge 'A' Jn (via Stewarts Lane)
Neighbouring ELRs: ['AHG', 'ATL', 'BML1', 'BSF', 'BSP2', 'CKL', 'FLL1', 'FLL2', 'RDG1', 'SLC8', 'VIR', 'VTB1']
Neighbour count:   12
 1  AHG   Waterloo Curve - Nine Elms Jn to Linford Street Jn
 2  ATL   Atlantic (or South London) Line - Peckham Rye to Battersea Park Jn
 3  BML1  London Waterloo to Weymouth - London Waterloo to Northam Jn
 4  BSF   Battersea Pier Jn to Factory Jn - 
 5  BSP2  Battersea Pier Jn to Pouparts Jn - Longhedge 'B' Jn to Pouparts Jn
 6  CKL   Culvert Road Jn to Latchmere Jn - 
 7  FLL1  Longhedge 'A' Jn to Clapham Jn (western side) - Longhedge 'A' Jn to Factory Jn
 8  FLL2  Longhedge 'A' Jn to Clapham Jn (western side) - Longhedge 'A' Jn to Lavender Hill Jn
 9  RDG1  London Waterloo to Reading - Waterloo (Windsor Lines) to Wokingham Jn
10  SLC8  Stewarts Lane Depot - Carriage Depot (Electrified Roads 1-22)
11  VIR   London Victoria to Ramsgate Line - London Victoria (Eastern Lines) to Ramsgate (via Herne Hill and Chatham)
12  VTB1  London Victoria to Brighton Main Line - London Victoria to Windmill Bridge Jn

ELR:               SPC8
Route:             London St Pancras to Chesterfield - Midland Main Line (MML)
Section:           Derby London Road Jn to Clay Cross South Jn
Neighbouring ELRs: ['AJM1', 'DBP1', 'DJW', 'LED', 'SPC6', 'SPC7', 'SPC9', 'TCC']
Neighbour count:   8
 1  AJM1  Matlock Branch - Ambergate Jn to Matlock Riverside
 2  DBP1  Birmingham and Derby Line - London Road Jn to Kingsbury Jn
 3  DJW   Wirksworth Branch - Duffield Jn to Wirksworth Incline
 4  LED   Little Eaton Jn to Derby - 
 5  SPC6  London St Pancras to Chesterfield - Midland Main Line (MML) - Ratcliffe Jn to Derby Jn
 6  SPC7  London St Pancras to Chesterfield - Midland Main Line (MML) - Spondon to Derby London Road Jn
 7  SPC9  London St Pancras to Chesterfield - Midland Main Line (MML) - Clay Cross South Jn to Tapton Jn
 8  TCC   Erewash Valley (or Toton to Clay Cross) Line - Trent East Jn to Clay Cross South Jn
"""
