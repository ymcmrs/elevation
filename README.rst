Global geographic elevation data made easy.
At the moment elevation provides easy download, cache and access of the global
`SRTM 90m Digital Elevation Database v4.1 <http://www.cgiar-csi.org/data/srtm-90m-digital-elevation-database-v4-1>`_
elaborated by CGIAR-CSI.

Installation and command line usage
-----------------------------------

You need to have the
`GDAL/OGR library and command line tools <https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries>`_
installed.

Install the `latest version of elevation <https://pypi.python.org/pypi/elevation>`_
from the Python Package Index::

    $ pip install elevation

Identify the bounding box of the area of interest and fetch the DEM with the ``eio`` command.
For example to clip the DEM of the area of Rome, 42N 12.5W, to the ``Rome-DEM.tif`` file execute::

    $ eio clip -o Rome-DEM.tif 12 41.5 13 42.5

The bounding box must be given as ``xmin ymin xmax ymax`` similarly to the ``rio`` command form ``rasterio``.

The first time an area is accessed elevation downloads the data tiles from the CGIAR-CSI server and
caches them as GeoTiff compressed formats,
subsequent accesses to the same and nearby areas are much faster.

Project resources
-----------------

============= ======================
Support       https://stackoverflow.com/search?q=python+elevation
Development   https://github.com/bopen/elevation
Download      https://pypi.python.org/pypi/elevation
============= ======================


Contributing
------------

Contributions are very welcome. Please see the `CONTRIBUTING`_ document for
the best way to help.
If you encounter any problems, please file an issue along with a detailed description.

.. _`CONTRIBUTING`: https://github.com/bopen/elevation/blob/master/CONTRIBUTING.rst

Authors:

- Alessandro Amici - `@alexamici <https://github.com/alexamici>`_

Sponsors:

- .. image:: http://services.bopen.eu/bopen-logo.png
      :target: http://bopen.eu/
      :alt: B-Open Solutions srl


License
-------

elevation is free and open source software
distributed under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.
