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

from . import cgiar_csi


def clip(output='out.tif', bounds=None, dataset='SRTM3', provider='CGIAR-CSI', version='V41'):
    left, bottom, right, top = bounds
    assert left <= right and bottom <= top
    if dataset == 'SRTM3' and provider == cgiar_csi.PROVIDER and version in ['V41']:
        kwargs = {'dataset': dataset, 'provider': provider, 'version': version}
        return cgiar_csi.srtm3_clip(bounds, output, **kwargs)

    raise ValueError("Unknown provider/dataset/version: %r/%r/%r" % (provider, dataset, version))
