Global geographic elevation data made easy.
Elevation provides easy download, cache and access of the global datasets
`SRTM 30m Global 1 arc second V003 <https://lpdaac.usgs.gov/dataset_discovery/measures/measures_products_table/SRTM1_v003>`_
elaborated by NASA and NGA
and
`SRTM 90m Digital Elevation Database v4.1 <http://www.cgiar-csi.org/data/srtm-90m-digital-elevation-database-v4-1>`_
elaborated by CGIAR-CSI.

Installation
------------

Install the `latest version of Elevation <https://pypi.python.org/pypi/elevation>`_
from the Python Package Index::

    $ pip install elevation

The following dependencies need to be installed and working:

- `GNU make <https://www.gnu.org/software/make/>`_
- `curl <https://curl.haxx.se/>`_
- unzip
- `GDAL command line tools <http://www.gdal.org/>`_

The following command runs some basic checks and reports common issues::

    $ eio selfcheck
    Your system is ready.


Command line usage
------------------

Identify the geographic bounds of the area of interest and fetch the DEM with the ``eio`` command.
For example to clip the SRTM1 30m DEM of the area of Rome, around 42N 12.5W, to the ``Rome-DEM.tif`` file::

    $ eio clip -o Rome-DEM.tif --bounds 12.35 41.8 12.65 42

The ``--bounds`` option accepts latitude and longitude coordinates
(more precisely in geodetic coordinates in the WGS84 refernce system EPSG:4326 for those who care)
given as ``left bottom right top`` similarly to the ``rio`` command form ``rasterio``.

The first time an area is accessed Elevation downloads the data tiles from the USGS or CGIAR-CSI servers and
caches them in GeoTiff compressed formats,
subsequent accesses to the same and nearby areas are much faster.

It is possible to pre-populate the cache for an area, for example to seed the SRTM3 90m DEM of Italy execute::

    $ eio seed --product SRTM3 --bounds 6.6 36.6 18.6 47.1


Python API
----------

Every command has a corresponding API function in the ``elevation`` module::

    import elevation

    # clip the SRTM1 30m DEM of the area around Rome and save it to Rome-DEM.tif
    elevation.clip(bounds=(12, 41.5, 13, 42.5), output='Rome-DEM.tif')

    # seed the SRTM3 90m DEM of Italy
    elevation.seed(product='SRTM3', bounds=(6.6 36.6 18.6 47.1))

See the `User's guide <http://elevation.bopen.eu/en/stable/usersguide.html>`_ for the complete list of functionalities.


Project resources
-----------------

============= =========================================================
Documentation http://elevation.bopen.eu
Support       https://stackoverflow.com/search?q=python+elevation
Development   https://github.com/bopen/elevation
Download      https://pypi.python.org/pypi/elevation
Code quality  .. image:: https://api.travis-ci.org/bopen/elevation.svg?branch=master
                :target: https://travis-ci.org/bopen/elevation/branches
                :alt: Build Status on Travis CI
              .. image:: https://coveralls.io/repos/bopen/elevation/badge.svg?branch=master&service=github
                :target: https://coveralls.io/github/bopen/elevation
                :alt: Coverage Status on Coveralls
============= =========================================================


Contributing
------------

Contributions are very welcome. Please see the `CONTRIBUTING`_ document for
the best way to help.
If you encounter any problems, please file an issue along with a detailed description.

.. _`CONTRIBUTING`: https://github.com/bopen/elevation/blob/master/CONTRIBUTING.rst

Authors:

- B-Open Solutions srl - `@bopen <https://github.com/bopen>`_ - http://bopen.eu
- Alessandro Amici - `@alexamici <https://github.com/alexamici>`_


License
-------

Elevation is free and open source software
distributed under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.
