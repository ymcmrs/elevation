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

import subprocess


def selfcheck():
    try:
        assert b'GNU Make' in subprocess.check_output('make --version', shell=True)
    except:
        raise RuntimeError('Fatal: GNU Make not found in PATH.')

    try:
        assert b'curl' in subprocess.check_output('curl --version', shell=True)
    except:
        raise RuntimeError('Fatal: curl not found in PATH.')

    try:
        assert b'UnZip' in subprocess.check_output('unzip -v', shell=True)
    except:
        raise RuntimeError('Fatal: unzip not found in PATH.')

    try:
        assert b'GDAL' in subprocess.check_output('gdal_translate --version', shell=True)
    except:
        raise RuntimeError('Fatal: gdal_translate not found in PATH.')

    try:
        assert b'GDAL' in subprocess.check_output('gdalbuildvrt --version', shell=True)
    except:
        raise RuntimeError('Fatal: gdalbuildvrt not found in PATH.')
