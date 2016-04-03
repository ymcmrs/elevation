
0.9.10 (unreleased)
-------------------

- Added ``-r/--reference`` and ``-m/--margin`` options to define the bounds from a GDAL/OGR data source.
  Install the ``rasterio`` and ``fiona`` packages with ``pip`` to enable it.
  Issue `#14 <https://github.com/bopen/elevation/issues/14>`_.
- Enable reading defaults from environment variables prefixed with ``EIO``,
  e.g. ``EIO_PRODUCT=SRTM3`` and ``EIO_CLIP_MARGIN=10%``.


0.9.9 (2016-04-01)
------------------

- Enforce the no-bulk-download policy.


0.9.8 (2016-03-31)
------------------

- Make ``clean`` remove empty tiles as they may be due to temporary server failures.


0.9.7 (2016-03-30)
------------------

- Fixed user visible documentation.


0.9.6 (2016-03-30)
------------------

- Initial public beta release.
