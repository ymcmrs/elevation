# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

from elevation import cgiar_csi


def test_srtm3_tile_ilonlat():
    # values from http://srtm.csi.cgiar.org/SELECTION/inputCoord.asp
    assert cgiar_csi.srtm3_tile_ilonlat(-177.5, 52.5) == (1, 2)
    assert cgiar_csi.srtm3_tile_ilonlat(177.5, -47.5) == (72, 22)
    assert cgiar_csi.srtm3_tile_ilonlat(10.1, 44.9) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(14.9, 44.9) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(10.1, 40.1) == (39, 4)
    assert cgiar_csi.srtm3_tile_ilonlat(14.9, 40.1) == (39, 4)


def test_srtm3_tiles_names():
    assert next(cgiar_csi.srtm3_tiles_names(10.1, 44.9, 10.1, 44.9)).endswith('srtm_39_04.tif')
    assert len(list(cgiar_csi.srtm3_tiles_names(9.9, 39.1, 15.1, 45.1))) == 9


def test_srtm3_ensure_setup(tmpdir):
    root = tmpdir.join('root')
    cgiar_csi.srtm3_ensure_setup(str(root), dataset='SRTM3', provider=cgiar_csi.PROVIDER, version='V41')


def test_srtm3_ensure_tiles(mocker):
    check_call = mocker.stub()
    cmd = cgiar_csi.srtm3_ensure_tiles('/tmp', ['a', 'b'], make_flags='-s', check_call=check_call)
    assert cmd == 'make -C /tmp -s all ENSURE_TILES="a b"'
    check_call.assert_called_once_with(cmd, shell=True)


def test_srtm3_do_clip(mocker):
    check_call = mocker.stub()
    cmd = cgiar_csi.srtm3_do_clip('/tmp', '/tmp/out.tif', [1, 5, 2, 6], make_flags='-s', check_call=check_call)
    assert cmd == 'make -C /tmp -s clip OUT_PATH="/tmp/out.tif" PROJWIN="1 6 2 5"'
    check_call.assert_called_once_with(cmd, shell=True)


def test_srtm3_clip():
    cgiar_csi.srtm3_clip(13.1, 43.1, 14.9, 44.9, 'out.tif') == 0
