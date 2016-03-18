# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import contextlib
import os
from future.moves.urllib import request

import rasterio


@contextlib.contextmanager
def urlretrieve_tempfile(url, filename=None):
    filename, info = request.urlretrieve(url, filename=filename)
    yield filename, info
    os.unlink(filename)


def is_valid_raster(datasource):
    try:
        with rasterio.open(datasource):
            pass
        return True
    except:
        return False


def build_datasource(datasource_path, glob_pattern='srtm_*.tif'):
    datasource_folder = os.path.dirname(datasource_path)
    build_cmd = 'gdalbuildvrt -overwrite %s %s' % (os.path.basename(datasource_path), glob_pattern)
    os.system('cd %s && %s' % (datasource_folder, build_cmd))
