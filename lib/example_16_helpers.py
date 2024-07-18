# Examples of multiple helper functions in the Geofurlong class.

from geofurlong import Geofurlong


gf = Geofurlong()

print("[gf.valid_elr]")
elrs = ("LEC3", "SOY", "NEM7", "ZZB2", "", "lec3", "soy", "NEM 7", "SOY ", "engineer's_line_reference")
for elr in elrs:
    print(f"Is ELR '{elr}' valid? {gf.valid_elr(elr)}")

print("\n[gf.valid_mile]")
miles = (-999, -99, 0, 50, 75, 150, 999)
for mile in miles:
    print(f"Is mile {mile} valid? {gf.valid_mile(mile)}")

print("\n[gf.valid_yard]")
yards = (-9999, -999, -50, 0, 1, 25, 1759, 1760)
for yard in yards:
    print(f"Is yard {yard} valid? {gf.valid_yard(yard)}")

print("\n[gf.build_total_yards]")
miles_yards = ((0, 0), (0, 1), (0, 1759), (1, 0), (9, 1759), (10, 0), (10, 1), (100, 0), (0, -1), (0, -100))
for my in miles_yards:
    print(f"Total yards for {my} is {gf.build_total_yards(my[0], my[1])}")

print("\n[gf.miles_yards_to_total_yards]")
mys = (0.0000, 0.0001, -0.0001, 0.1759, 1.0, 1.0001, 5.044, 5.088, 5.132, 9.1759, 10.0, 10.0001, 100.0001, 100.1759)
for my in mys:
    print(f"Total yards for {my} is {gf.miles_yards_to_total_yards(my)}")

print("\n[gf.explode_total_yards]")
total_yards = (0, 1, 1759, 1760, 1761, 9999)
for ty in total_yards:
    print(f"Exploded yards for {ty} is {gf.split_total_yards(ty)}")

print("\n[gf.mileage_verbose - at a point]")
miles_yards = ((0, 0), (0, 1), (0, 1759), (1, 0), (9, 1759), (10, 0), (10, 1), (100, 0), (0, -1), (0, -100))
for my in miles_yards:
    print(f"Verbose mileage for {my} is {gf.mileage_verbose(my[0], my[1], my[0], my[1])}")

print("\n[gf.mileage_verbose - between points]")
miles_yards = ((0, 0, 0, 1), (0, 1759, 1, 0), (9, 1759, 10, 0), (99, 440, 100, 1320), (0, -123, 0, -1))
for my in miles_yards:
    print(f"Verbose mileage for {my} is {gf.mileage_verbose(my[0], my[1], my[2], my[3])}")

print("\n[gf.km_verbose]")
kms = ((0, -123, 0, 0), (0, 500, 1, 999), (4, 123, 10, 1), (99, 999, 100, 1))
for km in kms:
    print(f"Verbose km for {km} is {gf.km_verbose(km[0], km[1], km[2], km[3])}")

print("\n[gf.format_mileage]")
mys = ((0, -123), (0, 0), (0, 1), (0, 1759), (1, 0), (9, 1759), (10, 0), (10, 1), (100, 0), (0, -1), (0, -100))
for my in mys:
    print(f"Formatted mileage for {my} is {gf.format_mileage(my[0], my[1])}")

print("\n[gf.format_total_yards]")
tys = (
    -199,
    -1,
    0,
    1,
    880,
    1759,
    1760,
    1761,
    4000,
    9999,
    10000,
    17600,
    17601,
    176000,
)
for ty in tys:
    print(f"Formatted total yards for {ty} is {gf.format_total_yards(ty)}")

print("\n[gf.total_yards_to_km]")
tys = (-219, -1, 0, 1, 11, 1094, 10936, 109361)
for ty in tys:
    print(f"Total yards to km for {ty} is {gf.total_yards_to_km(ty)}")

print("\n[gf.format_linear]")
tyms = ((-299, False), (0, False), (1759, False), (1760, False), (1094, True), (109361, True))
# def format_linear(total_yards: int, metric: bool) -> str:
for tym in tyms:
    print(f"Formatted linear for {tym[0]} (metric: {tym[1]}) is {gf.format_linear(tym[0], tym[1])}")

print("\n[gf.trackmap_coverage]")
for tm in range(1, 6):
    print(f"Trackmap coverage for Book {tm} is {gf.trackmap_coverage(tm)}")
