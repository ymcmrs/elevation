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
from __future__ import absolute_import, division, print_function, unicode_literals

import collections
import math
import os.path
import pkgutil

from . import util


def srtm3_tile_ilonlat(lon, lat):
    assert -180. <= lon <= 180. and -90. <= lat <= 90.
    ilon = int((math.floor(lon) + 180) // 5 + 1)
    ilat = int((64 - math.floor(lat)) // 5)
    return ilon, ilat


def srtmgl1_tile_ilonlat(lon, lat):
    assert -180. <= lon <= 180. and -90. <= lat <= 90.
    return int(math.floor(lon)), int(math.floor(lat))


def srtm3_tiles_names(left, bottom, right, top, tile_template='srtm_{ilon:02d}_{ilat:02d}.tif'):
    ileft, itop = srtm3_tile_ilonlat(left, top)
    iright, ibottom = srtm3_tile_ilonlat(right, bottom)
    for ilon in range(ileft, iright + 1):
        for ilat in range(itop, ibottom + 1):
            yield tile_template.format(**locals())


def srtmgl1_tiles_names(left, bottom, right, top, tile_name_template='{slat}{slon}.tif'):
    ileft, itop = srtmgl1_tile_ilonlat(left, top)
    iright, ibottom = srtmgl1_tile_ilonlat(right, bottom)
    for ilon in range(ileft, iright + 1):
        slon = '%s%03d' % ('E' if ilon >= 0 else 'W', abs(ilon))
        for ilat in range(ibottom, itop + 1):
            slat = '%s%02d' % ('N' if ilat >= 0 else 'S', abs(ilat))
            yield tile_name_template.format(**locals())


URL_TILES_DATASOURCE = pkgutil.get_data('elevation', 'url_tiles_datasource.mk').decode('utf-8')
URL_TILES_SPEC = dict(
    folders=('spool', 'cache'),
    file_templates={'Makefile': URL_TILES_DATASOURCE},
)

SRTMGL1_SPEC = URL_TILES_SPEC.copy()
SRTMGL1_SPEC.update(dict(
    datasource_url='http://e4ftl01.cr.usgs.gov/SRTM/SRTMGL1.003/2000.02.11',
    tile_ext='.hgt',
    zip_ext='.SRTMGL1.hgt.zip',
    tile_names=srtmgl1_tiles_names,
))

SRTM3_SPEC = URL_TILES_SPEC.copy()
SRTM3_SPEC.update(dict(
    datasource_url='http://srtm.csi.cgiar.org/SRT-ZIP/SRTM_V41/SRTM_Data_GeoTiff',
    tile_ext='.tif',
    zip_ext='.zip',
    tile_names=srtm3_tiles_names,
))

PRODUCTS_SPECS = collections.OrderedDict([
    ('SRTMGL1', SRTMGL1_SPEC),
    ('SRTM3', SRTM3_SPEC),
])
PRODUCTS = list(PRODUCTS_SPECS)


def ensure_tiles(path, ensure_tiles_names=(), **kwargs):
    ensure_tiles = ' '.join(ensure_tiles_names)
    variables_items = [('ensure_tiles', ensure_tiles)]
    return util.check_call_make(path, targets=['download'], variables=variables_items, **kwargs)


def do_clip(path, bounds, output, **kwargs):
    left, bottom, right, top = bounds
    projwin = '%s %s %s %s' % (left, top, right, bottom)
    variables_items = [('output', output), ('projwin', projwin)]
    return util.check_call_make(path, targets=['clip'], variables=variables_items, **kwargs)


def seed(cache_dir, product, bounds, **kwargs):
    datasource_root = os.path.join(cache_dir, product)
    spec = PRODUCTS_SPECS[product]
    util.ensure_setup(datasource_root, product=product, **spec)
    ensure_tiles_names = spec['tile_names'](*bounds)
    ensure_tiles(datasource_root, ensure_tiles_names, **kwargs)
    util.check_call_make(datasource_root, targets=['all'])
    return datasource_root


def clip(cache_dir, product, bounds, output, **kwargs):
    datasource_root = seed(cache_dir, product, bounds, **kwargs)
    do_clip(datasource_root, bounds, output, **kwargs)
