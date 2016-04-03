# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 B-Open Solutions srl - http://bopen.eu
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

import rasterio
import fiona


def import_bounds(reference):
    # ASSUMPTION: rasterio and fiona bounds are given in geodetic WGS84 crs
    try:
        with rasterio.open(reference) as datasource:
            bounds = datasource.bounds
    except:
        with fiona.open(reference) as datasource:
            bounds = datasource.bounds
    return bounds
