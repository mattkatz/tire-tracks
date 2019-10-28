#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tire_tracks` package."""

import pytest


from tire_tracks.tire_tracks import TireTracks
from zipfile import ZipFile
from pathlib import Path
from tempfile import TemporaryDirectory

# setup
td = TemporaryDirectory()
temp_path = Path(td.name)
z = ZipFile((temp_path / "test_wheel.whl"), "w")
for token in ["foo", "bar", "blah"]:
    tokenp = temp_path / (token + ".py")
    tokenp.write_text("pass")
    z.write(tokenp)
z.close()
w = Path(z.filename)


@pytest.fixture
def wheel():
    """ return a zipfile like a wheel"""
    return w


def test_creates_working_dir_with_fake(wheel):
    t = TireTracks(wheel, ".")
    with t.create_working_dir(wheel) as wd:
        assert wd.is_dir()
