# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import math
import os
import pkgutil

from . import USER_CACHE_DIR
from . import DATASOURCE_TEMPLATE
from . import util


PROVIDER = 'CGIAR-CSI'
SRTM3_TILE_NAME_TEMPLATE = 'srtm_{ilon:02d}_{ilat:02d}.tif'


def srtm3_tile_ilonlat(lon, lat):
    assert -180. <= lon <= 180. and -90. <= lat <= 90.
    ilon = int((math.floor(lon) + 180) // 5 + 1)
    ilat = int((64 - math.floor(lat)) // 5)
    return ilon, ilat


def srtm3_tiles_names(left, bottom, right, top, tile_name_template=SRTM3_TILE_NAME_TEMPLATE):
    ileft, itop = srtm3_tile_ilonlat(left, top)
    iright, ibottom = srtm3_tile_ilonlat(right, bottom)
    for ilon in range(ileft, iright + 1):
        for ilat in range(itop, ibottom + 1):
            yield tile_name_template.format(**locals())


def srtm3_ensure_setup(cache_dir, datasource_template, **kwargs):
    folders = ['cache', 'spool']
    file_templates = {
        'Makefile': pkgutil.get_data('elevation', 'cgiar_csi_srtm3.mk').decode('utf-8'),
    }
    datasource = datasource_template.format(**kwargs)
    datasource_root = os.path.join(cache_dir, datasource)
    util.ensure_setup(datasource_root, folders, file_templates, datasource=datasource, **kwargs)
    return datasource_root


def srtm3_ensure_tiles(path, ensure_tiles_names):
    ensure_tiles = ' '.join(ensure_tiles_names)
    util.call_make(path, targets=['all'], variables=locals(), make_flags='-j 4')


def srtm3_do_clip(path, out_path, bounds):
    left, bottom, right, top = bounds
    projwin = '%s %s %s %s' % (left, top, right, bottom)
    util.call_make(path, targets=['clip'], variables=locals())


def srtm3_clip(left, bottom, right, top, out_path, dataset='SRTM3', provider=PROVIDER, version='V41'):
    datasource_root = srtm3_ensure_setup(
        USER_CACHE_DIR, DATASOURCE_TEMPLATE, dataset=dataset, provider=provider, version=version)
    ensure_tiles_names = srtm3_tiles_names(left, bottom, right, top)
    srtm3_ensure_tiles(datasource_root, ensure_tiles_names)
    srtm3_do_clip(datasource_root, out_path, (left, bottom, right, top))
