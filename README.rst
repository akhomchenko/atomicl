=======
atomicl
=======

.. image:: https://travis-ci.org/gagoman/atomicl.svg?branch=master
   :target: https://travis-ci.org/gagoman/atomicl
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
pure Python fallback available *(you do not want to use it)*.

Examples::

    >> counter = atomicl.AtomicLong()
    >> counter += 2
    >> counter.value
    2
    >> counter.get_and_set(5)
    2
    >> counter.value
    5

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

Results for benchmarks.py_ on OS X ``10.13.5`` with
``Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz`` and turbo boost disabled:

``Python 3.7.0``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.py37] 1.50 us +- 0.04 us -> [atomicl_cy.py37] 92.3 ns +- 0.9 ns: 16.25x faster (-94%)
    ctor: Mean +- std dev: [atomic.py37] 1.40 us +- 0.02 us -> [atomicl_cy.py37] 109 ns +- 1 ns: 12.90x faster (-92%)
    increment: Mean +- std dev: [atomic.py37] 515 ns +- 7 ns -> [atomicl_cy.py37] 33.3 ns +- 0.3 ns: 15.43x faster (-94%)
    decrement: Mean +- std dev: [atomic.py37] 516 ns +- 6 ns -> [atomicl_cy.py37] 33.3 ns +- 0.2 ns: 15.51x faster (-94%)
    setter: Mean +- std dev: [atomic.py37] 1.56 us +- 0.02 us -> [atomicl_cy.py37] 42.0 ns +- 0.6 ns: 37.05x faster (-97%)
    cas: Mean +- std dev: [atomic.py37] 1.68 us +- 0.02 us -> [atomicl_cy.py37] 137 ns +- 1 ns: 12.30x faster (-92%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.py37] 1.50 us +- 0.04 us -> [atomicl_py.py37] 957 ns +- 17 ns: 1.57x faster (-36%)
    ctor: Mean +- std dev: [atomic.py37] 1.40 us +- 0.02 us -> [atomicl_py.py37] 902 ns +- 17 ns: 1.56x faster (-36%)
    increment: Mean +- std dev: [atomic.py37] 515 ns +- 7 ns -> [atomicl_py.py37] 980 ns +- 60 ns: 1.90x slower (+90%)
    decrement: Mean +- std dev: [atomic.py37] 516 ns +- 6 ns -> [atomicl_py.py37] 970 ns +- 26 ns: 1.88x slower (+88%)
    setter: Mean +- std dev: [atomic.py37] 1.56 us +- 0.02 us -> [atomicl_py.py37] 413 ns +- 12 ns: 3.77x faster (-73%)
    cas: Mean +- std dev: [atomic.py37] 1.68 us +- 0.02 us -> [atomicl_py.py37] 1.03 us +- 0.01 us: 1.64x faster (-39%)

``Python 3.4.6``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.py34] 1.64 us +- 0.06 us -> [atomicl_cy.py34] 74.5 ns +- 0.8 ns: 22.03x faster (-95%)
    ctor: Mean +- std dev: [atomic.py34] 1.52 us +- 0.03 us -> [atomicl_cy.py34] 90.9 ns +- 1.1 ns: 16.71x faster (-94%)
    increment: Mean +- std dev: [atomic.py34] 523 ns +- 20 ns -> [atomicl_cy.py34] 33.3 ns +- 0.3 ns: 15.70x faster (-94%)
    decrement: Mean +- std dev: [atomic.py34] 522 ns +- 7 ns -> [atomicl_cy.py34] 33.6 ns +- 0.3 ns: 15.55x faster (-94%)
    setter: Mean +- std dev: [atomic.py34] 1.42 us +- 0.04 us -> [atomicl_cy.py34] 44.0 ns +- 1.1 ns: 32.37x faster (-97%)
    cas: Mean +- std dev: [atomic.py34] 1.54 us +- 0.03 us -> [atomicl_cy.py34] 118 ns +- 1 ns: 13.05x faster (-92%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.py34] 1.64 us +- 0.06 us -> [atomicl_py.py34] 982 ns +- 28 ns: 1.67x faster (-40%)
    ctor: Mean +- std dev: [atomic.py34] 1.52 us +- 0.03 us -> [atomicl_py.py34] 912 ns +- 24 ns: 1.67x faster (-40%)
    increment: Mean +- std dev: [atomic.py34] 523 ns +- 20 ns -> [atomicl_py.py34] 1.09 us +- 0.02 us: 2.09x slower (+109%)
    decrement: Mean +- std dev: [atomic.py34] 522 ns +- 7 ns -> [atomicl_py.py34] 1.10 us +- 0.02 us: 2.11x slower (+111%)
    setter: Mean +- std dev: [atomic.py34] 1.42 us +- 0.04 us -> [atomicl_py.py34] 456 ns +- 6 ns: 3.12x faster (-68%)
    cas: Mean +- std dev: [atomic.py34] 1.54 us +- 0.03 us -> [atomicl_py.py34] 1.04 us +- 0.02 us: 1.48x faster (-33%)

``PyPy 5.8.0-6.0.0``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.pypy3] 292 ns +- 7 ns -> [atomicl_cy.pypy3] 1.20 us +- 0.04 us: 4.10x slower (+310%)
    ctor: Mean +- std dev: [atomic.pypy3] 270 ns +- 10 ns -> [atomicl_cy.pypy3] 1.13 us +- 0.03 us: 4.19x slower (+319%)
    increment: Mean +- std dev: [atomic.pypy3] 27.9 ns +- 0.4 ns -> [atomicl_cy.pypy3] 68.4 ns +- 2.8 ns: 2.45x slower (+145%)
    decrement: Mean +- std dev: [atomic.pypy3] 27.7 ns +- 0.1 ns -> [atomicl_cy.pypy3] 67.6 ns +- 1.0 ns: 2.44x slower (+144%)
    setter: Mean +- std dev: [atomic.pypy3] 283 ns +- 5 ns -> [atomicl_cy.pypy3] 49.4 ns +- 1.3 ns: 5.73x faster (-83%)
    cas: Mean +- std dev: [atomic.pypy3] 289 ns +- 6 ns -> [atomicl_cy.pypy3] 142 ns +- 7 ns: 2.03x faster (-51%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.pypy3] 292 ns +- 7 ns -> [atomicl_py.pypy3] 427 ns +- 12 ns: 1.46x slower (+46%)
    ctor: Mean +- std dev: [atomic.pypy3] 270 ns +- 10 ns -> [atomicl_py.pypy3] 390 ns +- 10 ns: 1.44x slower (+44%)
    increment: Mean +- std dev: [atomic.pypy3] 27.9 ns +- 0.4 ns -> [atomicl_py.pypy3] 274 ns +- 2 ns: 9.82x slower (+882%)
    decrement: Mean +- std dev: [atomic.pypy3] 27.7 ns +- 0.1 ns -> [atomicl_py.pypy3] 283 ns +- 6 ns: 10.19x slower (+919%)
    setter: Mean +- std dev: [atomic.pypy3] 283 ns +- 5 ns -> [atomicl_py.pypy3] 0.22 ns +- 0.00 ns: 1258.80x faster (-100%)
    cas: Mean +- std dev: [atomic.pypy3] 289 ns +- 6 ns -> [atomicl_py.pypy3] 268 ns +- 3 ns: 1.08x faster (-7%)

License
-------
MIT


.. _AtomicLong: https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/atomic/AtomicLong.html
.. _atomic: https://github.com/cyberdelia/atomic
.. _Cython: http://cython.org
.. _CFFI: https://cffi.readthedocs.io
.. _benchmarks.py: https://github.com/gagoman/atomicl/blob/master/benchmarks.py
