# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

# python 2 support via python-future
from __future__ import absolute_import, unicode_literals

from elevation import util


def test_ensure_setup(tmpdir):
    root = tmpdir.join('root')
    root_path = str(root)
    created_folders, _ = util.ensure_setup(root_path)
    assert len(created_folders) == 1 and created_folders[0].endswith('root')
    assert len(tmpdir.listdir()) == 1

    folders = ['etc', 'lib']
    created_folders, _ = util.ensure_setup(root_path, folders=folders)
    assert len(created_folders) == 2
    assert created_folders[0].endswith('etc')
    assert created_folders[1].endswith('lib')
    assert len(root.listdir()) == 2

    file_templates = [
        ('Makefile', 'all: {target}')
    ]
    created_folders, created_files = util.ensure_setup(root_path, folders=folders, file_templates=file_templates, target='file.txt')
    assert len(created_folders) == 0
    assert len(created_files) == 1
    assert len(root.listdir()) == 3
    assert root.join('Makefile').read() == 'all: file.txt'

    created_folders, created_files = util.ensure_setup(root_path, folders=folders, file_templates=file_templates, target='wrong')
    assert len(created_folders) == 0
    assert len(created_files) == 0
    assert len(root.listdir()) == 3
    assert root.join('Makefile').read() == 'all: file.txt'
