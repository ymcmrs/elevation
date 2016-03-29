
User's guide
============

.. warning:: This section is work in progress and there will be areas that are lacking.

Installation
------------

Install the `latest version of elevation <https://pypi.python.org/pypi/elevation>`_
from the Python Package Index::

    $ pip install elevation


Basic usage
-----------


Advanced usage
--------------


Command line reference
----------------------

The ``eio`` command as the following sub-commands and options::

    $ eio --help
    Usage: eio [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      clean      Clean up the cache from temporary files.
      clip       Clip the DEM to given bounds.
      seed       Seed the DEM to given bounds.
      selfcheck  Audits your installation for common issues.

The ``seed`` sub-command::

    $ eio seed --help
    Usage: eio seed [OPTIONS]

    Options:
      --product [SRTM1|SRTM3]    DEM product choice (default: 'SRTM1').
      --cache_dir DIRECTORY      Root of the DEM cache folder (default:
                                 '$HOME/Library/Caches/elevation').
      --make_flags TEXT          Options to be passed to make (default: '-s -k').
      --bounds FLOAT...          Output bounds: left bottom right top.
      --help                     Show this message and exit.

The ``clip`` sub-command::

    $ eio clip --help
    Usage: eio clip [OPTIONS]

    Options:
      --product [SRTM1|SRTM3]  DEM product choice (default: 'SRTM1').
      --cache_dir DIRECTORY      Root of the DEM cache folder (default:
                                 '$HOME/Library/Caches/elevation').
      --make_flags TEXT          Options to be passed to make (default: '-s -k').
      -o, --output PATH          Path to output file. Existing files will be
                                 overwritten.
      --bounds FLOAT...          Output bounds: left bottom right top.
      --help                     Show this message and exit.
