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

import click

from . import USER_CACHE_DIR
from . import api


# disable overzealous warning
click.disable_unicode_literals_warning = True


@click.group()
def eio():
    pass


@eio.command(short_help='Clip a DEM to given bounds.')
@click.option('-o', '--output', default='out.tif', type=click.Path(resolve_path=True, dir_okay=False),
              help="Path to output file. Existing files will be overwritten.")
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
@click.option('--make_flags', default='-k -s',
              help='Options to be passed to make.')
@click.option('--cache_dir', default=USER_CACHE_DIR,
              type=click.Path(resolve_path=True, file_okay=False),
              help='Root of the cache folder.')
def clip(**kwargs):
    api.clip(**kwargs)


@eio.command(short_help='Seed a DEM to given bounds.')
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
@click.option('--make_flags', default='-k -s',
              help='Options to be passed to make.')
@click.option('--cache_dir', default=USER_CACHE_DIR,
              type=click.Path(resolve_path=True, file_okay=False),
              help='Root of the cache folder.')
def seed(**kwargs):
    api.seed(**kwargs)
