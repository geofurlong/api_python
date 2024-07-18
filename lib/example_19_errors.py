# Examples of error propagation and handling in the Geofurlong class.

import os
import sqlite3
from geofurlong import Geofurlong


def database_not_available():
    current_dir = os.getcwd()

    # Deliberately move to a directory that does not contain the GeoFurlong SQLite database.
    os.chdir("..")
    try:
        _ = Geofurlong()
    except sqlite3.OperationalError as e:
        print(f"Unable to open the GeoFurlong SQLite database.\n{e}")
    finally:
        os.chdir(current_dir)


def invalid_elr():
    gf = Geofurlong()
    try:
        _ = gf.elr("abc9")
    except ValueError as e:
        print(f"\nInvalid ELR code.\n{e}")


def unknown_elr():
    gf = Geofurlong()
    try:
        _ = gf.elr("ABC9")
    except ValueError as e:
        print(f"\nUnknown ELR code.\n{e}")


def invalid_mileage_on_elr_at():
    gf = Geofurlong()
    try:
        _ = gf.at("LEC1", 1760 * 300)
    except ValueError as e:
        print(f"\nInvalid mileage on ELR.\n{e}")


def invalid_mileage_on_elr_between():
    gf = Geofurlong()
    try:
        _ = gf.between("NBK", 0, 1)
    except ValueError as e:
        print(f"\nInvalid mileage on ELR.\n{e}")

    try:
        _ = gf.between("NBK", 31900, 1760 * 50)
    except ValueError as e:
        print(f"\nInvalid mileage on ELR.\n{e}")


def invalid_iterator():
    gf = Geofurlong()
    try:
        for _ in gf.traverse("SBO", 0):
            pass
    except (ValueError, TypeError) as e:
        print(f"\nInvalid iterator specified.\n{e}")

    try:
        for _ in gf.traverse("SBO", "a"):
            pass
    except TypeError as e:
        print(f"\nInvalid iterator specified.\n{e}")


if __name__ == "__main__":
    database_not_available()
    invalid_elr()
    unknown_elr()
    invalid_mileage_on_elr_at()
    invalid_mileage_on_elr_between()
    invalid_iterator()
