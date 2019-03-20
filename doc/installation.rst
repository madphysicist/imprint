.. imprint: a program for creating documents from data and content templates

.. Copyright (C) 2019  Joseph R. Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>

.. This program is free software: you can redistribute it and/or modify
.. it under the terms of the GNU Affero General Public License as
.. published by the Free Software Foundation, either version 3 of the
.. License, or (at your option) any later version.

.. This program is distributed in the hope that it will be useful,
.. but WITHOUT ANY WARRANTY; without even the implied warranty of
.. MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.. GNU Affero General Public License for more details.

.. You should have received a copy of the GNU Affero General Public License
.. along with this program.  If not, see <https://www.gnu.org/licenses/>.

.. Author: Joseph Fox-Rabinovitz <jfoxrabinovitz at gmail dot com>
.. Version: 13 Apr 2019: Initial Coding


.. _installation:

==================
Installation Guide
==================

Imprint is available via `pypi`_, so the easiest way to install it is probably
with ::

    pip install imprint

Imprint uses `setuptools`_, so you can install it from source as well. If you
have a copy of the source distribution, run ::

    python setup.py install

from the root directory, with the appropriate privileges.

You can do the same thing with :program:`pip` if you prefer. Any of the
following should work, depending on how you obtained your distribution ::

    pip install git+<URL>/imprint.git@master   # For a remote git repository
    pip install imprint.zip                    # For an archived file
    pip install imprint/                       # For an unpacked folder or repo

See the page about :doc:`dependencies` for a complete description of additional
software that may need to be installed. Using :program:`setup.py` or
:program:`pip` should take care of all the Python dependencies.


------
Extras
------

To ensure that optional dependencies are included in the install, do ::

    pip install imprint[all]

The ``all`` extra option will include PDF, LaTeX and Pandas in the dependencies.


.. _installation-demos:

-----
Demos
-----

Imprint is packaged with a set of demo projects intended primarily for the
:doc:`tutorials/tutorials`. The demos are not normally installed as part of
Imprint, Instead, they are to be accessed through the source repository or the
documentation :ref:`installation-documentation`, once that is built.


.. _installation-tests:

-----
Tests
-----

Imprint does not currently have any formal unit tests available. However,
running through all of the demos serves as a non-automated set of tests, since
they exercise nearly every part of Imprint. Eventually, pytest-compatible tests
will be added in the :py:mod:`~imprint.tests` package.


.. _installation-documentation:

-------------
Documentation
-------------

If you intend to build the documentation, you can install the required addtional
dependencies like Sphinx using one of the appropriate extras ::

    pip install imprint[docs]

or ::

    pip install imprint[docs-rtd]

The documentation can be built from the source distribution by using the
specially defined command::

    python setup.py build_sphinx

Alternatively (perhaps preferably), it can be built using the provided Makefile:

    cd doc
    make html

Both options work on Windows and Unix-like systems that have :program:`make`
installed. The Windows version does not require :program:`make`.

Building the documentation will also make a copy of the
:ref:`installation-demos`.


.. include:: /link-defs.rst
