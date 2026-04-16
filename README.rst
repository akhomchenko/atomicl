=======
atomicl
=======

.. image:: https://github.com/akhomchenko/atomicl/actions/workflows/ci.yml/badge.svg?branch=master
   :target: https://github.com/akhomchenko/atomicl/actions/workflows/ci.yml
   :alt: CI Status

.. image:: https://img.shields.io/pypi/v/atomicl.svg
    :target: https://pypi.org/project/atomicl/#history
    :alt: Latest released version

.. image:: https://img.shields.io/pypi/pyversions/atomicl.svg
    :target: https://pypi.org/project/atomicl
    :alt: Supported Python versions

Yet another implementation of AtomicLong class.

Introduction
------------

Class that allows to update long value atomically.
Highly inspired by Java's AtomicLong_ class and atomic_ package.
The most of performance is gained by using Cython_ with the
pure Python fallback available.

Examples::

    >> counter = atomicl.AtomicLong()
    >> counter += 2
    >> counter.value
    2
    >> counter.get_and_set(5)
    2
    >> counter.value
    5

Supported Python Versions
-------------------------

``atomicl`` currently supports CPython ``3.11`` through ``3.14``.

Development Workflow
--------------------

The project uses uv_ for local environment management, testing, and
building.

Bootstrap a development environment::

    uv sync

The documented local workflow assumes the default ``dev`` group is
installed via ``uv sync`` before running lint, tests, benchmarks, or
packaging commands from a checkout, so Cython is available there when
needed for Cython-backed packaging workflows.

Run the test suite on the default interpreter::

    uv run pytest

Run lint::

    uv run flake8

Run the test suite on a specific supported interpreter::

    uv run --python 3.11 -m pytest
    uv run --python 3.12 -m pytest
    uv run --python 3.13 -m pytest
    uv run --python 3.14 -m pytest

Build source and wheel distributions::

    uv build

Smoke-test the benchmark entrypoint and benchmark dependencies::

    uv run --group benchmark python benchmarks.py --help

Run a faster local benchmark pass for one implementation::

    uv run --group benchmark python benchmarks.py --fast --impl atomicl_cy

Regenerate ``src/atomicl/_cy.c`` after editing ``src/atomicl/_cy.pyx``::

    uv sync
    uv build

Build Behavior
--------------

The package keeps an optional Cython-backed extension for the fast path
and retains the pure Python fallback for environments where the native
extension cannot be compiled.

Building the native extension requires a working C compiler toolchain.

Source distributions ship generated C code for the extension, so end
systems installing from the released sdist do not need Cython just to
build the package.

When packaging from a checkout with uv_, the local build uses
``src/atomicl/_cy.pyx`` and regenerates ``src/atomicl/_cy.c`` before
compiling the extension.

When Cython is not available, the build falls back to ``src/atomicl/_cy.c``.
If the extension build fails, installation falls back to the pure Python
implementation.

Differences from atomic_
------------------------

``atomic`` is a more mature library and is battle-tested.

Despite small API differences, the huge difference between ``atomic``
and ``atomicl`` is comparisons operations support. ``atomicl`` does
not supports comparison and, for now, I do not see reasons to have
it. I tend to agree with folks from java on
`this topic <https://stackoverflow.com/questions/7567502/why-are-two-atomicintegers-never-equal>`_.

``atomic`` is backed by CFFI_ which makes it a good choice for ``CPython``
and ``PyPy``. ``atomicl`` with ``Cython`` extension gains better
performance on ``CPython`` and performs worse on ``PyPy``. See
Benchmarks_ for more details.

Benchmarks
----------

Run ``benchmarks.py`` to compare the pure Python and Cython-backed
implementations on your current machine.

License
-------
MIT


.. _AtomicLong: https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/atomic/AtomicLong.html
.. _atomic: https://github.com/cyberdelia/atomic
.. _Cython: http://cython.org
.. _CFFI: https://cffi.readthedocs.io
.. _uv: https://docs.astral.sh/uv/
.. _benchmarks.py: https://github.com/akhomchenko/atomicl/blob/master/benchmarks.py
