# Example of traversing ELRs by yardage intervals and outputting co-ordinates in planar and geographic forms.

from geofurlong import Geofurlong


gf = Geofurlong()

routes = (
    ("QLT1", 9),  # arbitrary yardage interval
    ("HPW", 110),  # sixteenth of mile
    ("MSG2", 220),  # eighth of mile
    ("PJW", 440),  # quarter of mile
    ("BOK5", 880),  # half mile
    ("EBW", 1760),  # mile
    ("BBJ", 1760 * 2),  # 2 miles
    ("WBS3", 1760 * 5),  # 5 miles
    ("SCU1", 1760 * 10),  # 10 miles
    ("MLN1", 1760 * 25),  # 25 miles
)

for elr, yardage_interval in routes:
    print(f"\nCo-ordinates of ELR {elr} at maximum {yardage_interval} yard intervals")
    print("ELR   Mileage     Easting      Northing     Longitude   Latitude")

    for total_yards in gf.traverse(elr, yardage_interval):
        miles, yards = gf.split_total_yards(total_yards)
        easting_northing = gf.at(elr, miles * 1760 + yards, lon_lat=False)
        geographic = gf.at(elr, miles * 1760 + yards, lon_lat=True)
        mileage = gf.format_mileage(miles, yards)
        print(
            f"{elr:<4}  {mileage:<10} {easting_northing.x:>11.3f}m {easting_northing.y:>11.3f}m  {geographic.x:>9.6f}°  {geographic.y:>9.6f}°"
        )


"""
Co-ordinates of ELR QLT1 at maximum 9 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
QLT1  3M 1494y    524315.871m  183131.907m  -0.209103°  51.533415°
QLT1  3M 1497y    524313.246m  183131.337m  -0.209141°  51.533411°
QLT1  3M 1506y    524305.369m  183129.629m  -0.209255°  51.533397°
QLT1  3M 1515y    524297.495m  183127.909m  -0.209369°  51.533383°
QLT1  3M 1524y    524289.677m  183125.942m  -0.209483°  51.533367°
QLT1  3M 1533y    524281.854m  183123.974m  -0.209596°  51.533351°
QLT1  3M 1542y    524274.031m  183122.006m  -0.209709°  51.533335°
QLT1  3M 1551y    524266.208m  183120.038m  -0.209823°  51.533319°
QLT1  3M 1560y    524258.385m  183118.070m  -0.209936°  51.533303°
QLT1  3M 1569y    524250.783m  183115.608m  -0.210047°  51.533283°

Co-ordinates of ELR HPW at maximum 110 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
HPW   0M -055y    531371.178m  188266.788m  -0.105527°  51.577963°
HPW   0M 0000y    531376.208m  188216.662m  -0.105473°  51.577512°
HPW   0M 0110y    531386.004m  188116.421m  -0.105369°  51.576609°
HPW   0M 0220y    531364.112m  188019.075m  -0.105721°  51.575739°
HPW   0M 0330y    531302.051m  187940.559m  -0.106646°  51.575048°
HPW   0M 0440y    531215.065m  187890.515m  -0.107919°  51.574618°
HPW   0M 0550y    531121.729m  187840.500m  -0.109284°  51.574191°
HPW   0M 0660y    531025.799m  187795.149m  -0.110684°  51.573805°
HPW   0M 0704y    530987.427m  187777.009m  -0.111244°  51.573651°

Co-ordinates of ELR MSG2 at maximum 220 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
MSG2  0M -297y    541558.917m  297940.062m   0.086847°  52.560887°
MSG2  0M -220y    541566.461m  297991.362m   0.086980°  52.561346°
MSG2  0M 0000y    541588.017m  298137.935m   0.087361°  52.562657°
MSG2  0M 0220y    541552.512m  298276.973m   0.086897°  52.563915°
MSG2  0M 0440y    541445.796m  298379.867m   0.085367°  52.564867°
MSG2  0M 0660y    541340.992m  298484.847m   0.083867°  52.565838°
MSG2  0M 0880y    541255.058m  298604.283m   0.082651°  52.566933°
MSG2  0M 1100y    541198.081m  298740.957m   0.081869°  52.568175°
MSG2  0M 1320y    541148.693m  298878.508m   0.081199°  52.569424°
MSG2  0M 1540y    541113.655m  299020.879m   0.080743°  52.570712°
MSG2  1M 0000y    541108.792m  299168.934m   0.080734°  52.572043°
MSG2  1M 0035y    541108.019m  299192.488m   0.080733°  52.572255°

Co-ordinates of ELR PJW at maximum 440 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
PJW   0M -001y    394820.024m  298707.827m  -2.077887°  52.586150°
PJW   0M 0000y    394819.388m  298708.128m  -2.077897°  52.586153°
PJW   0M 0440y    394444.041m  298851.763m  -2.083439°  52.587440°
PJW   0M 0880y    394063.705m  298982.900m  -2.089055°  52.588615°
PJW   0M 1320y    393680.830m  299105.982m  -2.094709°  52.589717°
PJW   1M 0000y    393289.830m  299200.932m  -2.100483°  52.590566°
PJW   1M 0440y    392908.844m  299185.008m  -2.106106°  52.590418°
PJW   1M 0880y    392610.901m  298916.990m  -2.110498°  52.588005°
PJW   1M 1320y    392246.975m  298773.759m  -2.115866°  52.586712°
PJW   1M 1321y    392246.092m  298773.906m  -2.115879°  52.586713°

Co-ordinates of ELR BOK5 at maximum 880 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
BOK5  0M 0720y    521509.557m  182523.150m  -0.249752°  51.528554°
BOK5  0M 0880y    521439.704m  182394.645m  -0.250802°  51.527415°
BOK5  1M 0000y    521096.682m  181668.888m  -0.255994°  51.520966°
BOK5  1M 0880y    520807.308m  180919.056m  -0.260419°  51.514289°
BOK5  2M 0000y    520622.465m  180136.691m  -0.263349°  51.507297°
BOK5  2M 0880y    520286.388m  179411.932m  -0.268436°  51.500855°
BOK5  3M 0000y    519698.779m  178868.193m  -0.277082°  51.496092°
BOK5  3M 0880y    519021.125m  178435.401m  -0.286985°  51.492346°
BOK5  3M 1549y    518480.066m  178180.977m  -0.294860°  51.490172°

Co-ordinates of ELR EBW at maximum 1760 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
EBW   12M 1266y   322140.281m  199904.865m  -3.127826°  51.692474°
EBW   13M 0000y   322078.967m  200337.180m  -3.128810°  51.696352°
EBW   14M 0000y   321010.620m  201354.554m  -3.144495°  51.705348°
EBW   15M 0000y   320151.896m  202448.633m  -3.157170°  51.715061°
EBW   16M 0000y   319033.608m  203561.330m  -3.173612°  51.724903°
EBW   17M 0000y   318637.741m  205102.327m  -3.179703°  51.738698°
EBW   18M 0000y   317760.126m  206436.649m  -3.192725°  51.750564°
EBW   19M 0000y   317326.065m  207964.703m  -3.199376°  51.764236°
EBW   19M 1688y   317091.887m  209460.325m  -3.203126°  51.777646°

Co-ordinates of ELR BBJ at maximum 3520 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
BBJ   4M 1440y    528818.926m  173088.884m  -0.147878°  51.442152°
BBJ   6M 0000y    530654.530m  172595.058m  -0.121664°  51.437294°
BBJ   8M 0000y    533364.600m  171211.583m  -0.083218°  51.424231°
BBJ   10M 0000y   534856.627m  168745.362m  -0.062709°  51.401715°
BBJ   11M 1466y   537450.031m  169841.905m  -0.025025°  51.410947°

Co-ordinates of ELR WBS3 at maximum 8800 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
WBS3  17M 1738y   357912.302m  405618.961m  -2.636632°  53.545511°
WBS3  20M 0000y   355029.403m  406986.214m  -2.680333°  53.557560°
WBS3  25M 0000y   348527.424m  410939.997m  -2.779128°  53.592496°
WBS3  30M 0000y   341048.934m  413882.292m  -2.892658°  53.618150°
WBS3  35M 0000y   334254.170m  416860.571m  -2.995991°  53.644105°
WBS3  35M 0626y   333796.877m  417188.623m  -3.002977°  53.646995°

Co-ordinates of ELR SCU1 at maximum 17600 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
SCU1  11M 0397y   532829.172m  164471.260m  -0.093434°  51.363783°
SCU1  20M 0000y   538993.992m  153210.858m  -0.009324°  51.261120°
SCU1  30M 0000y   548538.562m  141063.988m   0.122347°  51.149567°
SCU1  40M 0000y   552680.366m  128602.960m   0.176255°  51.036508°
SCU1  46M 0547y   546982.568m  120814.236m   0.091898°  50.968002°

Co-ordinates of ELR MLN1 at maximum 44000 yard intervals
ELR   Mileage     Easting      Northing     Longitude   Latitude
MLN1  0M -021y    526703.800m  181233.002m  -0.175377°  51.515820°
MLN1  0M 0000y    526690.417m  181246.700m  -0.175565°  51.515946°
MLN1  25M 0000y   487592.149m  180313.370m  -0.739090°  51.514964°
MLN1  50M 0000y   456822.841m  187946.888m  -1.181218°  51.587520°
MLN1  75M 0000y   418376.323m  186571.377m  -1.736211°  51.577710°
MLN1  100M 0000y  384457.907m  169182.241m  -2.224907°  51.421436°
MLN1  125M 0000y  350165.394m  169735.101m  -2.718134°  51.424422°
MLN1  150M 0000y  331110.394m  139511.243m  -2.986314°  51.150696°
MLN1  175M 0000y  306988.801m  116677.042m  -3.325228°  50.942006°
MLN1  200M 0000y  296510.444m   85470.352m  -3.465515°  50.659683°
MLN1  225M 0000y  276975.899m   60461.167m  -3.733496°  50.431077°
MLN1  246M 0565y  247155.765m   55261.621m  -4.150953°  50.377339°
"""
