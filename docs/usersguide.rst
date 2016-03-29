
User's guide
============

.. warning:: This section is work in progress and there will be areas that are lacking.


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

GNU make, curl and unzip come pre-installed with most operating systems.
The best way to install GDAL command line tools varies across operating systems
and distributions, please refer to the
`GDAL install documentation <https://trac.osgeo.org/gdal/wiki/DownloadingGdalBinaries>`_.


Command line usage
------------------


Python API
----------


Command line reference
----------------------

The ``eio`` command as the following sub-commands and options::

    $ eio --help
    Usage: eio [OPTIONS] COMMAND [ARGS]...

    Options:
      --product [SRTM1|SRTM3]  DEM product choice (default: 'SRTM1').
      --cache_dir DIRECTORY    Root of the DEM cache folder (default:
                               '/Users/amici/Library/Caches/elevation').
      --make_flags TEXT        Options to be passed to make (default: '-s -k').
      --help                   Show this message and exit.

    Commands:
      clean      Clean up the cache from temporary files.
      clip       Clip the DEM to given bounds.
      distclean  Clean up the cache from temporary files.
      info
      seed       Seed the DEM to given bounds.
      selfcheck  Audits your installation for common issues.

The ``seed`` sub-command::

    $ eio seed --help
    Usage: eio seed [OPTIONS]

    Options:
      --bounds FLOAT...  Output bounds: left bottom right top.
      --help             Show this message and exit.

The ``clip`` sub-command::

    $ eio clip --help
    Usage: eio clip [OPTIONS]

    Options:
      -o, --output PATH  Path to output file. Existing files will be overwritten.
      --bounds FLOAT...  Output bounds: left bottom right top.
      --help             Show this message and exit.

