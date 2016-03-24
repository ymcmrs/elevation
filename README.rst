Global geographic elevation data made easy.
elevation provides easy download, cache and access of the global datasets
`SRTMGL1 30m Global 1 arc second V003 <https://lpdaac.usgs.gov/dataset_discovery/measures/measures_products_table/srtmgl1_v003>`_
elaborated by NASA and NGA
and
`SRTM 90m Digital Elevation Database v4.1 <http://www.cgiar-csi.org/data/srtm-90m-digital-elevation-database-v4-1>`_
elaborated by CGIAR-CSI.

Installation
------------

Install the `latest version of elevation <https://pypi.python.org/pypi/elevation>`_
from the Python Package Index::

    $ pip install elevation

The following dependencies need to be installed and working:

- `GNU make <https://www.gnu.org/software/make/>`_
- `curl <https://curl.haxx.se/>`_
- unzip
- `GDAL command line tools <http://www.gdal.org/>`_

The following command runs some basic checks and reports common issues::

    $ eio selfcheck


Command line usage
------------------

Identify the geographic bounds of the area of interest and fetch the DEM with the ``eio`` command.
For example to clip the SRTMGL1 30m DEM of the area of Rome, around 42N 12.5W, to the ``Rome-DEM.tif`` file::

    $ eio clip -o Rome-DEM.tif --bounds 12 41.5 13 42.5

The ``--bounds`` option must be given as ``left bottom right top`` similarly to the ``rio`` command form ``rasterio``.

The first time an area is accessed elevation downloads the data tiles from the USGS or CGIAR-CSI servers and
caches them in GeoTiff compressed formats,
subsequent accesses to the same and nearby areas are much faster.

It is possible to pre-populate the cache for an area, for example to seed the SRTM3 90m DEM of Italy execute::

    $ eio seed --product SRTM3 --bounds 6.6 36.6 18.6 47.1


Python API
----------

Every command have a corresponding API function in the ``elevation`` module::

    import elevation

    # clip the SRTMGL1 30m DEM of the area around Rome and save it to Rome-DEM.tif
    elevation.clip(bounds=(12, 41.5, 13, 42.5), output='Rome-DEM.tif')

    # seed the SRTM3 90m DEM of Italy
    elevation.seed(product='SRTM3', bounds=(6.6 36.6 18.6 47.1))


Project resources
-----------------

============= ======================
Documentation https://bopen-elevation.readthedocs.org
Support       https://stackoverflow.com/search?q=python+elevation
Development   https://github.com/bopen/elevation
Download      https://pypi.python.org/pypi/elevation
Code quality  .. image:: https://api.travis-ci.org/bopen/elevation.svg?branch=master
                :target: https://travis-ci.org/bopen/elevation/branches
                :alt: Build Status on Travis CI
              .. image:: https://coveralls.io/repos/bopen/elevation/badge.svg?branch=master&service=github
                :target: https://coveralls.io/github/bopen/elevation
                :alt: Coverage Status on Coveralls
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
