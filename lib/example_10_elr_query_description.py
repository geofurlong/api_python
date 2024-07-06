# Example of querying description all available ELRs in database.

from geofurlong import Geofurlong


gf = Geofurlong()

elrs = gf.elr_codes

print(f"GeoFurlong database version {gf.db_version} contains {len(elrs)} ELRs")


def search(search_text: str) -> None:
    print(f"\nList ELRs with '{search_text}' in the Route or Section description\n")
    print("ELR    Route                                     Section")
    print("-" * 110)

    for elr in elrs:
        candidate = gf.elr(elr)
        route = candidate.route
        section = candidate.section
        if (search_text in route) or (search_text in section):
            print(f"{candidate.elr:4}   {candidate.route:40}  {candidate.section}")


search("Harbour")
search("Hull")
search("Portobello")

"""
GeoFurlong database version 6.8.1 contains 1588 ELRs

List ELRs with 'Harbour' in the Route or Section description

ELR    Route                                     Section
--------------------------------------------------------------------------------------------------------------
ARH    Ardrossan Harbour Branch                  Holm Jn to Ardrossan Harbour
AYH1   Ayr Harbour Branch                        Newton Jn to Ayr Harbour (NR boundary)
AYH2   Ayr Harbour Branch                        Falkland Jn to Ayr Harbour Jn (via Falkland Yard)
BHB    Bristol Harbour Branch                    
CWR    Cattewater Branch                         Cattewater Jn to Cattewater Harbour (NR boundary)
FFH1   Folkestone Harbour Branch                 Folkestone East Jn to Limit of Headshunt for Harbour Branch
FFH2   Folkestone Harbour Branch                 Folkestone East Yard Jn to Folkestone Harbour
FSH    Fishguard Harbour Lines                   NR boundary to Fishguard Harbour sidings
HAR    King’s Lynn Harbour Branch                
INS    Inverness Harbour Branch                  Inverness Harbour Branch Jn to Inverness Harbour NR boundary
MHH    Heysham Branch                            Morecombe Jn to Heysham Harbour
NHB    Newhaven Harbour (or Marine) Branch       Newhaven Harbour Jn to Newhaven Harbour
SEA1   Seafields Branch                          Dawdon Jn to Seaham Harbour NR boundary
STN    Stranraer Harbour Jn to Stranraer Town    
STR1   Stranraer Harbour Branch                  Ayr to Girvan
STR2   Stranraer Harbour Branch                  Girvan to former Challoch Jn
STR3   Stranraer Harbour Branch                  former Challoch Jn to Stranraer Harbour Jn (or Yard)
STR4   Stranraer Harbour Branch                  Stranraer Harbour Jn (or Yard) to Stranraer
SUT1   Sutton Harbour Branch (Plymouth)          Laira Jn to Mount Gold Jn
SUT2   Sutton Harbour Branch (Plymouth)          Mount Gold Jn to former Friary Jn
WPH2   Havant Jn to Portsmouth Harbour           

List ELRs with 'Hull' in the Route or Section description

ELR    Route                                     Section
--------------------------------------------------------------------------------------------------------------
HBS    Hull to Seamer West Jn (via Bridlington)  West Parade Jn to Seamer West Jn
HUL1   Leeds to Hull                             Hull to Selby
HUL2   Leeds to Hull                             Selby to Selby South Jn
HUL3   Leeds to Hull                             Selby South Jn to near Micklefield (former Regional boundary)
HUL4   Leeds to Hull                             near Micklefield (former Regional boundary) to Leeds
PHC    Priory Yard to Hull Central Goods Line    Hessle East Jn to Dairycoates

List ELRs with 'Portobello' in the Route or Section description

ELR    Route                                     Section
--------------------------------------------------------------------------------------------------------------
LHS1   Leith South Branch                        Portobello Jn to Leith South Jn
NDE1   Portobello Jn to Millerhill South Jn (via former Niddrie North Jn)  
PJW    Portobello Loop (Wolverhampton)           Portobello Jn to Heath Town Jn to Crane Street Jn
SUB1   Edinburgh South Suburban (Sub) Line       Portobello Jn to former Niddrie North Jn
"""
