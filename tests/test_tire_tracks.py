#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `tire_tracks` package."""

import pytest


from tire_tracks.tire_tracks import TireTracks
from zipfile import ZipFile
from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture
def wheel():
    """ return a zipfile like a wheel"""
    td = TemporaryDirectory()
    temp_path = Path(td.name)
    z = ZipFile((temp_path / "test_wheel.whl"), "w")
    for token in ["foo", "bar", "blah"]:
        tokenp = temp_path / (token + ".py")
        tokenp.write_text("pass")
        z.write(tokenp)
    z.close()
    return Path(z.filename)


def test_creates_working_dir_with_fake():
    td = TemporaryDirectory()
    temp_path = Path(td.name)
    z = ZipFile((temp_path / "test_wheel.whl"), "w")
    for token in ["foo", "bar", "blah"]:
        tokenp = temp_path / (token + ".py")
        tokenp.write_text("pass")
        z.write(tokenp)
    z.close()
    wheel = Path(z.filename)
    t = TireTracks(wheel, ".")
    with t.create_working_dir(wheel) as wd:
        assert wd.is_dir()
    wd2 = t.create_working_dir(wheel)
    assert wd2.is_dir()

