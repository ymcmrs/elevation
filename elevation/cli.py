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

import functools

import click

import elevation
from . import util


# disable overzealous warning
click.disable_unicode_literals_warning = True


@click.group()
@click.version_option()
@click.option('--product', default=elevation.DEFAULT_PRODUCT, type=click.Choice(elevation.PRODUCTS),
              help='DEM product choice (default: %r).' % elevation.DEFAULT_PRODUCT)
@click.option('--cache_dir', default=elevation.CACHE_DIR,
              type=click.Path(resolve_path=True, file_okay=False),
              help='Root of the DEM cache folder (default: %r).' % elevation.CACHE_DIR)
def eio(**kwargs):
    pass


@eio.command(short_help='Audits your installation for common issues.')
def selfcheck():
    print(util.selfcheck(tools=elevation.TOOLS))


def click_merge_parent_params(wrapped):
    @click.pass_context
    @functools.wraps(wrapped)
    def wrapper(ctx, **kwargs):
        if ctx.parent and ctx.parent.params:
            kwargs.update(ctx.parent.params)
        return wrapped(**kwargs)
    return wrapper


@eio.command(short_help='')
@click_merge_parent_params
def info(**kwargs):
    elevation.info(**kwargs)


@eio.command(short_help='Seed the DEM to given bounds.')
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
@click_merge_parent_params
def seed(**kwargs):
    elevation.seed(**kwargs)


try:
    # NOTE: GDAL/OGR bindings are not supported on Pypy
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
except ImportError:
    def import_bounds(reference):
        raise click.BadOptionUsage("-r/--reference disabled, to enable it install rasterio and fiona.")


def ensure_bounds(wrapped):
    @functools.wraps(wrapped)
    def wrapper(bounds, reference, **kwargs):
        if not bounds:
            if not reference:
                raise ValueError("bounds are not defined.")
            else:
                bounds = import_bounds(reference)
        return wrapped(bounds=bounds, **kwargs)
    return wrapper


@eio.command(short_help='Clip the DEM to given bounds.')
@click.option('-o', '--output', default=elevation.DEFAULT_OUTPUT,
              type=click.Path(resolve_path=True, dir_okay=False),
              help="Path to output file. Existing files will be overwritten.")
@click.option('--bounds', nargs=4, type=float, default=None,
              help='Output bounds: left bottom right top.')
@click.option('-m', '--margin', default=elevation.MARGIN,
              help="Decimal degree margin added to the bounds. Use '%%' for percent margin. "
              "Defaults to %r" % elevation.MARGIN)
@click.option('-r', '--reference',
              help="Use the extent of a reference GDAL/OGR data source as output bounds.")
@ensure_bounds
@click_merge_parent_params
def clip(bounds, **kwargs):
    elevation.clip(bounds, **kwargs)


@eio.command(short_help='Clean up the cache from temporary files.')
@click_merge_parent_params
def clean(**kwargs):
    elevation.clean(**kwargs)


@eio.command(short_help='Clean up the cache from temporary files.')
@click_merge_parent_params
def distclean(**kwargs):
    elevation.distclean(**kwargs)
