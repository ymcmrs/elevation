
Design
======

This chapter documents the high-level design of the product and
it is intended for developers contributing to the project.

.. note:: **Users of the product need not bother with the following. Unless they are curious :)**


Mission and vision
------------------

The project mission is to enable easy management of global digital elevation data.

Target use cases:

#. access DEM data on-demand from well-known repositories
#. download and store efficiently elevation data on large areas

Project goals:

#. data download from well-known repositories
#. compact storage of local data


Software architecture
---------------------

Logical components:

- the datasource Makefile
- the Python API
- the ``eio`` CLI


Version goals
-------------

This project strives to adhere to `semantic versioning <http://semver.org>`_.


1.0.0 (upcoming release)
~~~~~~~~~~~~~~~~~~~~~~~~

Minimal set of features to be operationally useful.
No completeness and no performance guarantees.

- Cache management:

  - Auto setup

- Documentation:

  - Enough to inspire and raise interest in new users.

  - Enough to use it effectively and safely.
