# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import subprocess

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
    root_path = str(tmpdir.join('root'))
    cgiar_csi.srtm3_ensure_setup(root_path, dataset='SRTM3', provider=cgiar_csi.PROVIDER, version='V41')


def test_srtm3_ensure_tiles(mocker):
    with mocker.patch('subprocess.check_call'):
        cmd = cgiar_csi.srtm3_ensure_tiles('/', ['a', 'b'], make_flags='-s')
    assert cmd == 'make -C / -s download ENSURE_TILES="a b"'
    subprocess.check_call.assert_called_once_with(cmd, shell=True)


def test_srtm3_do_clip(mocker):
    bounds = (1, 5, 2, 6)
    with mocker.patch('subprocess.check_call'):
        cmd = cgiar_csi.srtm3_do_clip('/', '/out.tif', bounds, make_flags='-s')
    assert cmd == 'make -C / -s clip OUTPUT="/out.tif" PROJWIN="1 6 2 5"'
    subprocess.check_call.assert_called_once_with(cmd, shell=True)


def test_srtm3_seed(mocker, tmpdir):
    root = tmpdir.join('root')
    bounds = (13.1, 43.1, 14.9, 44.9)
    with mocker.patch('subprocess.check_call'):
        cgiar_csi.srtm3_seed(bounds, cache_dir=str(root))
    assert len(root.listdir()) == 1
    datasource_root = root.listdir()[0]
    expected_cmd = 'make -C %s  download ENSURE_TILES="srtm_39_04.tif"' % datasource_root
    subprocess.check_call.assert_any_call(expected_cmd, shell=True)


def test_srtm3_clip(mocker, tmpdir):
    root = tmpdir.join('root')
    bounds = (13.1, 43.1, 14.9, 44.9)
    with mocker.patch('subprocess.check_call'):
        cgiar_csi.srtm3_clip(bounds, 'out.tif', cache_dir=str(root))
    assert len(root.listdir()) == 1
    datasource_root = root.listdir()[0]
    expected_cmd = 'make -C %s  clip OUTPUT="out.tif" PROJWIN="13.1 44.9 14.9 43.1"' % datasource_root
    subprocess.check_call.assert_any_call(expected_cmd, shell=True)
