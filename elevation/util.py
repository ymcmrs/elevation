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

import collections
import os
import subprocess


def ensure_setup(root, folders=(), file_templates=(), **kwargs):
    created_folders = []
    for path in [root] + [os.path.join(root, p) for p in folders]:
        if not os.path.exists(path):
            os.makedirs(path)
            created_folders.append(path)

    created_files = collections.OrderedDict()
    for relpath, template in collections.OrderedDict(file_templates).items():
        path = os.path.join(root, relpath)
        if not os.path.exists(path):
            body = template.format(**kwargs)
            with open(path, 'w') as file:
                file.write(body)
            created_files[path] = body

    return created_folders, created_files


def check_call_make(path, targets=(), variables=(), make_flags='', check_call=subprocess.check_call):
    make_targets = ' '.join(targets)
    variables_items = collections.OrderedDict(variables).items()
    make_variables = ' '.join('%s="%s"' % (k.upper(), v) for k, v in variables_items)
    cmd = 'make -C {path} {make_flags} {make_targets} {make_variables}'.format(**locals())
    check_call(cmd, shell=True)
    return cmd
