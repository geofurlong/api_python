# Basic performance testing.

from geofurlong import Geofurlong
import time


if __name__ == "__main__":
    gf = Geofurlong()

    elrs = ("AIW", "SDJ2", "PBN", "TBH1", "EGM1", "CWL2", "CBC1", "LEC1", "WCK", "MLN1")
    intervals = (22, 1_760)

    print("Run  ELR   Len (km)    Interval (y)  Lon_Lat  Iterations/second")

    for elr in elrs:
        elr_len_km = gf.elr(elr).measured_len_km
        for interval in intervals:
            for lon_lat in (False, True):
                for run in range(1, 3):
                    start_time = time.time()
                    for i, ty in enumerate(gf.traverse(elr, interval), start=1):
                        _ = gf.at(elr, ty, lon_lat=lon_lat)
                    end_time = time.time()
                    duration = end_time - start_time
                    iterations_per_second = i / duration

                    print(
                        f"{run}    {elr:4}   {elr_len_km:7.3f}            {interval:4}  {'True ' if lon_lat else 'False'}              {iterations_per_second:7.0f}"
                    )

"""
Run  ELR   Len (km)    Interval (y)  Lon_Lat  Iterations/second
1    AIW      0.136              22  False                34224
2    AIW      0.136              22  False                52211
1    AIW      0.136              22  True                 12901
2    AIW      0.136              22  True                 13176
1    AIW      0.136            1760  False                31775
2    AIW      0.136            1760  False                36472
1    AIW      0.136            1760  True                 12633
2    AIW      0.136            1760  True                 12886
1    SDJ2    14.088              22  False                37438
2    SDJ2    14.088              22  False                36976
1    SDJ2    14.088              22  True                 13105
2    SDJ2    14.088              22  True                 13372
1    SDJ2    14.088            1760  False                 9825
2    SDJ2    14.088            1760  False                 9204
1    SDJ2    14.088            1760  True                  6529
2    SDJ2    14.088            1760  True                  6227
1    PBN     27.780              22  False                43105
2    PBN     27.780              22  False                44432
1    PBN     27.780              22  True                 14293
2    PBN     27.780              22  True                 14323
1    PBN     27.780            1760  False                 8289
2    PBN     27.780            1760  False                 8980
1    PBN     27.780            1760  True                  5907
2    PBN     27.780            1760  True                  6250
1    TBH1    49.567              22  False                40443
2    TBH1    49.567              22  False                41421
1    TBH1    49.567              22  True                 13965
2    TBH1    49.567              22  True                 13965
1    TBH1    49.567            1760  False                 8094
2    TBH1    49.567            1760  False                 8343
1    TBH1    49.567            1760  True                  5911
2    TBH1    49.567            1760  True                  5032
1    EGM1    72.448              22  False                34685
2    EGM1    72.448              22  False                35975
1    EGM1    72.448              22  True                 13098
2    EGM1    72.448              22  True                 13405
1    EGM1    72.448            1760  False                 8114
2    EGM1    72.448            1760  False                 7914
1    EGM1    72.448            1760  True                  5178
2    EGM1    72.448            1760  True                  5448
1    CWL2    95.446              22  False                10311
2    CWL2    95.446              22  False                10253
1    CWL2    95.446              22  True                  6930
2    CWL2    95.446              22  True                  6928
1    CWL2    95.446            1760  False                 4896
2    CWL2    95.446            1760  False                 4568
1    CWL2    95.446            1760  True                  3559
2    CWL2    95.446            1760  True                  3763
1    CBC1   120.836              22  False                27929
2    CBC1   120.836              22  False                28190
1    CBC1   120.836              22  True                 12023
2    CBC1   120.836              22  True                 11961
1    CBC1   120.836            1760  False                 7082
2    CBC1   120.836            1760  False                 6842
1    CBC1   120.836            1760  True                  4879
2    CBC1   120.836            1760  True                  5479
1    LEC1   134.205              22  False                27142
2    LEC1   134.205              22  False                27414
1    LEC1   134.205              22  True                 11829
2    LEC1   134.205              22  True                 11797
1    LEC1   134.205            1760  False                 6994
2    LEC1   134.205            1760  False                 6504
1    LEC1   134.205            1760  True                  4670
2    LEC1   134.205            1760  True                  5508
1    WCK    260.044              22  False                21190
2    WCK    260.044              22  False                21171
1    WCK    260.044              22  True                 10568
2    WCK    260.044              22  True                 10521
1    WCK    260.044            1760  False                 6563
2    WCK    260.044            1760  False                 6285
1    WCK    260.044            1760  True                  4693
2    WCK    260.044            1760  True                  4856
1    MLN1   395.871              22  False                14215
2    MLN1   395.871              22  False                14221
1    MLN1   395.871              22  True                  8518
2    MLN1   395.871              22  True                  8378
1    MLN1   395.871            1760  False                 5819
2    MLN1   395.871            1760  False                 5862
1    MLN1   395.871            1760  True                  4660
2    MLN1   395.871            1760  True                  4615
"""