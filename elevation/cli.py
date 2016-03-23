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

import click

import elevation
from . import util


# disable overzealous warning
click.disable_unicode_literals_warning = True


@click.group()
def eio():
    pass


@eio.command(short_help='Audits your installation for common issues.')
def selfcheck():
    util.selfcheck(tools=elevation.TOOLS)


product_options = util.composed(
    click.option('--product', default=elevation.DEFAULT_PRODUCT, type=click.Choice(elevation.PRODUCTS),
                 help='DEM product choice (default: %r).' % elevation.DEFAULT_PRODUCT),
    click.option('--cache_dir', default=elevation.CACHE_DIR,
                 type=click.Path(resolve_path=True, file_okay=False),
                 help='Root of the DEM cache folder (default: %r).' % elevation.CACHE_DIR),
    click.option('--make_flags', default='-k -s',
                 help='Options to be passed to make (default: %r).' % elevation.MAKE_FLAGS),
)


@eio.command(short_help='Seed the DEM to given bounds.')
@product_options
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
def seed(**kwargs):
    elevation.seed(**kwargs)


@eio.command(short_help='Clip the DEM to given bounds.')
@product_options
@click.option('-o', '--output', default=elevation.DEFAULT_OUTPUT,
              type=click.Path(resolve_path=True, dir_okay=False),
              help="Path to output file. Existing files will be overwritten.")
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
def clip(**kwargs):
    elevation.clip(**kwargs)


@eio.command(short_help='Clean up the cache from temporary files.')
@product_options
def clean(**kwargs):
    elevation.clean(**kwargs)
