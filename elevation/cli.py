# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import click

from . import api


@click.group()
def eio():
    pass


@eio.command()
@click.argument('bbox', type=float, nargs=4)
@click.option('-o', '--out_path', type=click.Path(), default='out.tif')
def clip(**kwargs):
    api.clip(**kwargs)
