# -*- coding: utf-8 -*-

"""Main module."""
from pathlib import Path
from tempfile import TemporaryDirectory
from contextlib import contextmanager
from zipfile import ZipFile


class TireTracks():
    def __init__(self, wheel, outdir):
        self.wheelpath = Path(wheel)
        self.outdir = Path(outdir)

    def impress(self):
        # unzip the wheel to a temp directory
        # create a docs directory
        # run sphinx against the docs directory
        pass

    @contextmanager
    def create_working_dir(self, wheel: Path) -> Path:
        """Given a *wheel* Path, unzip to a temporary directory and return that working directory.

        :param wheel:
        :type wheel: Path
        :rtype: Path
        """

        wheelzip = ZipFile(wheel)
        # with a tempdir
        tempd = TemporaryDirectory()
        # unzip the wheel into tempdir
        # TODO: optimize this to only extract what we will need
        wheelzip.extractall(tempd.name)
        # yield for use as a Path
        yield Path(tempd.name)
        # let it get cleaned up
        return Path(tempd.name)
