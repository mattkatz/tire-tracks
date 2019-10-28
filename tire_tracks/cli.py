# -*- coding: utf-8 -*-

"""Console script for tire_tracks."""
import argparse
import sys
from tire_tracks import TireTracks


def main():
    """Console script for tire_tracks."""
    parser = argparse.ArgumentParser()
    parser.add_argument("wheel", help="path to a wheel to try documenting")
    parser.add_argument("dir", help="Path to a directory to put docs in")
    args = parser.parse_args()
    tt = TireTracks(args.wheel, args.dir)
    tt.impress()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
