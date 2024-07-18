# Example of querying groupings of ELRs.

from geofurlong import Geofurlong


gf = Geofurlong()


def view_grouping(target: str) -> None:
    target_elr = gf.elr(target)
    grouping = target_elr.grouping

    print(f"ELR:           {target_elr.elr}")
    print(f"ELRs in group: {grouping}")
    print(f"Group count:   {len(grouping)}")

    if len(grouping) > 1:
        for member in grouping:
            member_elr = gf.elr(member)
            print(f"{member_elr.elr:4} : {member_elr.route} - {member_elr.section}")

    else:
        print(f"ELR {target_elr.elr} is not part of a group of ELRs")


if __name__ == "__main__":
    target_elrs = ("NBK", "SDI1", "BML3", "HUL1", "MVL3", "SCM5", "CGJ7")
    for target_elr in target_elrs:
        view_grouping(target_elr)
        print()


    print("\nELRs within group of 5 or more ELRs:")
    large_groups = [elr for elr in gf.elr_codes if len(gf.elr(elr).grouping) >= 5]
    print(large_groups)


"""
ELR:           NBK
ELRs in group: ['']
Group count:   1
ELR NBK is not part of a group of ELRs

ELR:           SDI1
ELRs in group: ['SDI1', 'SDI2']
Group count:   2
SDI1 : Swansea District Line - Briton Ferry to Jersey Marine Jn (Up Flying Loop)
SDI2 : Swansea District Line - Jersey Marine Jn to Morlais Jn

ELR:           BML3
ELRs in group: ['BML1', 'BML2', 'BML3']
Group count:   3
BML1 : London Waterloo to Weymouth - London Waterloo to Northam Jn
BML2 : London Waterloo to Weymouth - Northam Jn to Dorchester Jn
BML3 : London Waterloo to Weymouth - Dorchester Jn to Weymouth

ELR:           HUL1
ELRs in group: ['HUL1', 'HUL2', 'HUL3', 'HUL4']
Group count:   4
HUL1 : Leeds to Hull - Hull to Selby
HUL2 : Leeds to Hull - Selby to Selby South Jn
HUL3 : Leeds to Hull - Selby South Jn to near Micklefield (former Regional boundary)
HUL4 : Leeds to Hull - near Micklefield (former Regional boundary) to Leeds

ELR:           MVL3
ELRs in group: ['MVL1', 'MVL2', 'MVL3', 'MVL4']
Group count:   4
MVL1 : Manchester Victoria to Huddersfield - Miles Platting Jn to Stalybridge Jn
MVL2 : Manchester Victoria to Huddersfield - Stalybridge Jn to Stalybridge
MVL3 : Manchester Victoria to Huddersfield - Stalybridge to Heaton Lodge Jn
MVL4 : Manchester Victoria to Huddersfield - Bradley Jn to Heaton Lodge East Jn

ELR:           SCM5
ELRs in group: ['SCM1', 'SCM2', 'SCM3', 'SCM4', 'SCM5']
Group count:   5
SCM1 : Scottish Central Main Line - Motherwell Jn to Mossend South Jn
SCM2 : Scottish Central Main Line - Mossend South Jn to Whifflet North Jn
SCM3 : Scottish Central Main Line - Whifflet North Jn to Dunblane (former Oban Jn)
SCM4 : Scottish Central Main Line - Dunblane (former Oban Jn) to Perth South Jn
SCM5 : Scottish Central Main Line - Dundee Central Jn to Perth South Jn

ELR:           CGJ7
ELRs in group: ['LEC1', 'LEC2', 'LEC3', 'LEC4', 'LEC5', 'LEC6', 'CGJ1', 'CGJ2', 'CGJ3', 'CGJ4', 'CGJ5', 'CGJ6', 'CGJ7', 'WCM1', 'WCM2']
Group count:   15
LEC1 : West Coast Main Line (WCML) - London Euston to Rugby Trent Valley Jn
LEC2 : West Coast Main Line (WCML) - Rugby Trent Valley Jn to Stafford Trent Valley Jn
LEC3 : West Coast Main Line (WCML) - Stafford Trent Valley Jn to Stafford North Jn
LEC4 : West Coast Main Line (WCML) - Stafford North Jn to Crewe 157.25 MP
LEC5 : West Coast Main Line (WCML) - Crewe 157.25 MP to 159 MP
LEC6 : West Coast Main Line (WCML) - Little Bridgeford Jn to Heamie’s Bridge [DS]; Little Bridgeford Jn to Searchlight Lane Jn [UNB]
CGJ1 : West Coast Main Line (WCML) - Crewe 159 MP to Weaver Jn
CGJ2 : West Coast Main Line (WCML) - Weaver Jn to Warrington South Jn
CGJ3 : West Coast Main Line (WCML) - Warrington South Jn to Winwick Jn
CGJ4 : West Coast Main Line (WCML) - Winwick Jn to Golborne Jn
CGJ5 : West Coast Main Line (WCML) - Golborne Jn to Preston
CGJ6 : West Coast Main Line (WCML) - Preston to Lancaster
CGJ7 : West Coast Main Line (WCML) - Lancaster to Carlisle
WCM1 : West Coast Main Line (WCML) - Carlisle to Law Jn
WCM2 : West Coast Main Line (WCML) - Law Jn to Glasgow Central


ELRs within group of 5 or more ELRs:
['AYR1', 'AYR2', 'AYR3', 'AYR4', 'AYR5', 'AYR6', 'BBS', 'BBS1', 'BBS2', 'BBS3', 'BBS4', 'BOK1', 'BOK2', 'BOK3', 'BOK4', 'BOK5', 'BOK6', 'BSD1', 'BSD2', 'BSD3', 'BSD4', 'BSD5', 'BSD6', 'BSD8', 'CGJ1', 'CGJ2', 'CGJ3', 'CGJ4', 'CGJ5', 'CGJ6', 'CGJ7', 'ECM1', 'ECM2', 'ECM3', 'ECM4', 'ECM5', 'ECM6', 'ECM7', 'ECM8', 'ECM9', 'ECN1', 'ECN2', 'ECN3', 'ECN4', 'ECN5', 'ELL1', 'ELL2', 'ELL3', 'ELL4', 'ELL5', 'EYD1', 'EYD2', 'EYD3', 'EYD4', 'EYD5', 'EYD6', 'EYD7', 'EYD8', 'EYD9', 'FHR1', 'FHR2', 'FHR3', 'FHR4', 'FHR5', 'FHR6', 'FTC', 'GSM1', 'GSM2', 'GSM3', 'GSM4', 'GSM5', 'GSM6', 'HGP4', 'HGP5', 'HGP6', 'HGP7', 'HGP8', 'HGP9', 'LEC1', 'LEC2', 'LEC3', 'LEC4', 'LEC5', 'LEC6', 'LMD1', 'LMD2', 'LMD3', 'LMD4', 'LMD5', 'LMD6', 'LMD7', 'LMD8', 'NBE', 'NEM1', 'NEM2', 'NEM3', 'NEM4', 'NEM5', 'NEM6', 'NEM7', 'SCM1', 'SCM2', 'SCM3', 'SCM4', 'SCM5', 'SPC1', 'SPC2', 'SPC3', 'SPC4', 'SPC5', 'SPC6', 'SPC7', 'SPC8', 'SPC9', 'SPD1', 'SPD2', 'SPD3', 'SPD4', 'SPD5', 'TRL1', 'TRL2', 'TRL3', 'TRL5', 'TRL6', 'TRL7', 'TRL8', 'WCM1', 'WCM2']
"""
