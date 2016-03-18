# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import math
import os
from future.moves.urllib import parse
import shutil
import subprocess
import zipfile

import elevation
from . import util


BASE_URL = 'http://srtm.csi.cgiar.org/'

SRTM3_TILES_FOLDER = 'SRT-ZIP/SRTM_{version}/SRTM_Data_GeoTiff/'
SRTM3_TILE_LOCAL_NAME = 'srtm_{ilon:02d}_{ilat:02d}.tif'
SRTM3_TILE_REMOTE_NAME = 'srtm_{ilon:02d}_{ilat:02d}.zip'


def srtm3_tile_ilonlat(lon, lat):
    assert -180. <= lon <= 180. and -90. <= lat <= 90.
    ilon = int((math.floor(lon) + 180) // 5 + 1)
    ilat = int((64 - math.floor(lat)) // 5)
    return ilon, ilat


def srtm3_tile_local_path(ilon, ilat, version='V41', local_root=elevation.USER_CACHE_DIR):
    tile_local_name = SRTM3_TILE_LOCAL_NAME.format(**locals())
    tiles_folder = SRTM3_TILES_FOLDER.format(**locals())
    tile_local_path = os.path.join(local_root, tiles_folder, tile_local_name)
    return tile_local_path


def srtm3_tile_remote_url(ilon, ilat, version='V41'):
    tile_remote_name = SRTM3_TILE_REMOTE_NAME.format(**locals())
    tiles_folder = SRTM3_TILES_FOLDER.format(**locals())
    tile_remote_url = parse.urljoin(BASE_URL, tiles_folder + tile_remote_name)
    return tile_remote_url


def srtm3_unpack_tile(zip_local_path, tile_local_path):
    with zipfile.ZipFile(zip_local_path) as zip, open(tile_local_path, 'wb') as tile:
        zipped = zip.open(os.path.basename(tile_local_path))
        shutil.copyfileobj(zipped, tile)
    return tile_local_path


def srtm3_fetch_tile(ilon, ilat, tile_local_path, version='V41'):
    tile_remote_url = srtm3_tile_remote_url(ilon, ilat, version=version)
    with util.urlretrieve_tempfile(tile_remote_url) as (zip_local_path, _):
        return srtm3_unpack_tile(zip_local_path, tile_local_path)


def srtm3_ensure_datasource(xmin, ymin, xmax, ymax, local_root=elevation.USER_CACHE_DIR, version='V41'):
    top_left = srtm3_tile_ilonlat(xmin, ymax)
    bottom_right = srtm3_tile_ilonlat(xmax, ymin)

    rebuild_datasource = False
    for ilon in range(top_left[0], bottom_right[0] + 1):
        for ilat in range(top_left[1], bottom_right[1] + 1):
            tile_local_path = srtm3_tile_local_path(ilon, ilat, local_root=local_root, version=version)
            subprocess.check_call('mkdir -p %s' % os.path.dirname(tile_local_path), shell=True)
            if not util.is_valid_raster(tile_local_path):
                rebuild_datasource = True
                srtm3_fetch_tile(ilon, ilat, tile_local_path, version=version)

    datasource_path = os.path.join(os.path.dirname(tile_local_path), 'cgiar-csi-srtm3.vrt')
    if rebuild_datasource:
        util.build_datasource(datasource_path)

    return datasource_path


def srtm3_clip(xmin, ymin, xmax, ymax, clip_path, local_root=elevation.USER_CACHE_DIR, version='V41'):
    datasource_path = srtm3_ensure_datasource(xmin, ymin, xmax, ymax, local_root=local_root, version=version)
    bbox_test = '%f %f %f %f' % (xmin, ymax, xmax, ymin)
    subprocess.check_call('gdal_translate -projwin %s %s %s' % (bbox_test, datasource_path, clip_path), shell=True)
