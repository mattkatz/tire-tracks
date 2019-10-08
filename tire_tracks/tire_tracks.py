# -*- coding: utf-8 -*-

"""Main module."""
from pathlib import Path


class TireTracks():
    def __init__(self, args):
        self.wheelpath = Path(args.wheel)
        self.outdir = Path(args.outdir)

    def impress(self):
        # unzip the wheel to a temp directory
        # create a docs directory
        # run sphinx against the docs directory
