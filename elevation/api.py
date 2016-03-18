# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Alessandro Amici
#

from . import cgiar_csi


def clip(bbox, out_path, dataset='srtm3', provider='cgiar-csi', version='V41'):
    xmin, ymin, xmax, ymax = bbox
    assert xmin <= xmax and ymin <= ymax
    if dataset.lower() == 'srtm3' and provider == 'cgiar-csi':
        return cgiar_csi.srtm3_clip(xmin, ymin, xmax, ymax, out_path, version=version)

    raise ValueError("Unknown dataset/version combination: %r/%r" % (dataset, version))
