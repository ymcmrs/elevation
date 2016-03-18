# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

import elevation


def clip(bbox, dataset='srtm3', provider='cgiar-csi', version='V41', local_root=elevation.USER_CACHE_DIR):
    from . import cgiar_csi
    xmin, ymin, xmax, ymax = bbox
    assert xmin <= xmax and ymin <= ymax
    if dataset.lower() == 'srtm3' and provider == 'cgiar-csi':
        return cgiar_csi.srtm3_clip(xmin, ymin, xmax, ymax, local_root=local_root, version=version)

    raise ValueError("Unknown dataset/version combination: %r/%r" % (dataset, version))
