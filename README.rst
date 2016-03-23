Global geographic elevation data made easy.
At the moment elevation provides easy download, cache and access of the global datasets
`SRTMGL1 30m Global 1 arc second V003 <https://lpdaac.usgs.gov/dataset_discovery/measures/measures_products_table/srtmgl1_v003>`_
elaborated by NASA and NGA
and
`SRTM 90m Digital Elevation Database v4.1 <http://www.cgiar-csi.org/data/srtm-90m-digital-elevation-database-v4-1>`_
elaborated by CGIAR-CSI.

Installation and command line usage
-----------------------------------

The following dependencies need to be installed:

- `GNU make <https://www.gnu.org/software/make/>`_
- `curl <https://curl.haxx.se/>`_
- unzip
- `GDAL command line tools <http://www.gdal.org/>`_

Install the `latest version of elevation <https://pypi.python.org/pypi/elevation>`_
from the Python Package Index::

    $ pip install elevation

Identify the geographic bounds of the area of interest and fetch the DEM with the ``eio`` command.
For example to clip the DEM of the area of Rome, 42N 12.5W, to the ``Rome-DEM.tif`` file::

    $ eio clip -o Rome-DEM.tif --bounds 12 41.5 13 42.5

The ``--bounds`` option must be given as ``left bottom right top`` similarly to the ``rio`` command form ``rasterio``.

The first time an area is accessed elevation downloads the data tiles from the CGIAR-CSI server and
caches them as GeoTiff compressed formats,
subsequent accesses to the same and nearby areas are much faster.

It is possible to pre-populate the cache for an area, for example for Italy execute::

    $ eio seed --bounds 6.6 36.6 18.6 47.1


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
