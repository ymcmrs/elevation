# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 B-Open Solutions srl - http://bopen.eu
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

import subprocess

import pytest

from elevation import util


def test_selfcheck():
    assert 'NAME' not in util.selfcheck([('NAME', 'true')])
    assert 'NAME' in util.selfcheck([('NAME', 'false')])


def test_folder_try_lock(tmpdir, mocker):
    root = tmpdir.join('root')

    @util.folder_try_lock
    def operation(path):
        return True

    assert operation(str(root))

    mocker.patch('fasteners.InterProcessLock.acquire', return_value=False)
    with pytest.raises(RuntimeError):
        operation(str(root))


def test_ensure_setup(tmpdir):
    root = tmpdir.join('root')
    root_path = str(root)
    created_folders, _ = util.ensure_setup(root_path)
    assert len(created_folders) == 0
    assert len(tmpdir.listdir()) == 1

    folders = ['etc', 'lib']
    created_folders, _ = util.ensure_setup(root_path, folders=folders)
    assert len(created_folders) == 2
    assert created_folders[0].endswith('etc')
    assert created_folders[1].endswith('lib')
    assert len(root.listdir()) == 3

    file_templates = [
        ('Makefile', 'all: {target}')
    ]
    created_folders, created_files = util.ensure_setup(
        root_path, folders=folders, file_templates=file_templates, target='file.txt')
    assert len(created_folders) == 0
    assert len(created_files) == 1
    assert len(root.listdir()) == 4
    assert root.join('Makefile').read() == 'all: file.txt'

    created_folders, created_files = util.ensure_setup(
        root_path, folders=folders, file_templates=file_templates, target='wrong')
    assert len(created_folders) == 0
    assert len(created_files) == 0
    assert len(root.listdir()) == 4
    assert root.join('Makefile').read() == 'all: file.txt'


def test_check_call_make(mocker):
    mocker.patch('subprocess.check_call')
    cmd = util.check_call_make('/tmp')
    assert cmd.strip() == 'make -C /tmp'
    subprocess.check_call.assert_called_once_with(cmd, shell=True)
