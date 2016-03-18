# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import os

from elevation import cgiar_csi


def test_srtm3_v41_tile_indices():
    # values from http://srtm.csi.cgiar.org/SELECTION/inputCoord.asp
    assert cgiar_csi.srtm3_tile_ilonlat(-177.5, 52.5) == (1, 2)
    assert cgiar_csi.srtm3_tile_ilonlat(177.5, -47.5) == (72, 22)
    assert cgiar_csi.srtm3_tile_ilonlat(10.1, 44.9) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(14.9, 44.9) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(10.1, 40.1) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(14.9, 40.1) == (39, 4)


def test_srtm3_tile_local_path():
    assert cgiar_csi.srtm3_tile_local_path(39, 4).endswith('srtm_39_04.tif')


def test_srtm3_tile_remote_url():
    # values from http://srtm.csi.cgiar.org/SELECTION/inputCoord.asp
    expected = 'http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff/srtm_39_04.zip'
    assert cgiar_csi.srtm3_tile_remote_url(39, 4) == expected


def test_srtm3_unpack_tile():
    here = os.path.dirname(__file__)
    cgiar_csi.srtm3_unpack_tile(os.path.join(here, 'srtm_39_04.zip'), os.path.join(here, 'srtm_39_04.tif'))


def notest_srtm3_fetch_tile():
    here = os.path.dirname(__file__)
    cgiar_csi.srtm3_fetch_tile(39, 4, os.path.join(here, 'srtm_39_04.tif'))


def test_srtm3_ensure_datasource():
    assert cgiar_csi.srtm3_ensure_datasource(9.1, 39.1, 14.9, 44.9)


def test_srtm3_clip():
    cgiar_csi.srtm3_clip(9.1, 39.1, 14.9, 44.9, 'out.tif') == 0
