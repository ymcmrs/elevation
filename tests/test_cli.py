# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 B-Open Solutions srl - http://bopen.eu
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import click.testing

import subprocess

from elevation import cli


def test_eio_selfcheck(mocker):
    runner = click.testing.CliRunner()
    with mocker.patch('subprocess.check_output'):
        result = runner.invoke(cli.selfcheck)
    assert not result.exception
    assert subprocess.check_output.call_count == 5


def test_eio_seed(mocker, tmpdir):
    root = tmpdir.join('root')
    runner = click.testing.CliRunner()
    options = '--cache_dir %s --bounds 12.5 42 12.5 42' % str(root)
    with mocker.patch('subprocess.check_call'):
        result = runner.invoke(cli.seed, options.split())
    assert not result.exception
    assert subprocess.check_call.call_count == 2


def test_eio_clip(mocker, tmpdir):
    root = tmpdir.join('root')
    runner = click.testing.CliRunner()
    options = '--cache_dir %s --bounds 12.5 42 12.5 42' % str(root)
    with mocker.patch('subprocess.check_call'):
        result = runner.invoke(cli.clip, options.split())
    assert not result.exception
    assert subprocess.check_call.call_count == 3


def test_eio_clean(mocker, tmpdir):
    root = tmpdir.join('root')
    runner = click.testing.CliRunner()
    options = '--cache_dir %s' % str(root)
    with mocker.patch('subprocess.check_call'):
        result = runner.invoke(cli.clean, options.split())
    assert not result.exception
    assert subprocess.check_call.call_count == 1


def test_eio(mocker, tmpdir):
    root = tmpdir.join('root')
    runner = click.testing.CliRunner()
    options = 'seed --cache_dir %s --bounds 12.5 42 12.5 42' % str(root)
    with mocker.patch('subprocess.check_call'):
        result = runner.invoke(cli.eio, options.split())
    assert not result.exception
    assert subprocess.check_call.call_count == 2
