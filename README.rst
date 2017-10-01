=======
atomicl
=======

.. image:: https://travis-ci.org/gagoman/atomicl.svg?branch=master
   :target: https://travis-ci.org/gagoman/atomicl
   :alt: CI Status

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

Results for benchmarks.py_ on OS X ``10.12.6 (16G29)`` with
``Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz`` and turbo boost disabled:

``Python 3.6.2``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.py36] 1.57 us +- 0.05 us -> [atomicl_cy.py36] 105 ns +- 4 ns: 14.96x faster (-93%)
    ctor: Mean +- std dev: [atomic.py36] 1.48 us +- 0.04 us -> [atomicl_cy.py36] 124 ns +- 6 ns: 12.01x faster (-92%)
    increment: Mean +- std dev: [atomic.py36] 557 ns +- 16 ns -> [atomicl_cy.py36] 35.9 ns +- 1.4 ns: 15.52x faster (-94%)
    decrement: Mean +- std dev: [atomic.py36] 552 ns +- 23 ns -> [atomicl_cy.py36] 35.9 ns +- 1.2 ns: 15.37x faster (-93%)
    setter: Mean +- std dev: [atomic.py36] 1.55 us +- 0.06 us -> [atomicl_cy.py36] 46.3 ns +- 0.9 ns: 33.41x faster (-97%)
    cas: Mean +- std dev: [atomic.py36] 1.78 us +- 0.04 us -> [atomicl_cy.py36] 153 ns +- 3 ns: 11.63x faster (-91%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.py36] 1.57 us +- 0.05 us -> [atomicl_py.py36] 1.10 us +- 0.02 us: 1.43x faster (-30%)
    ctor: Mean +- std dev: [atomic.py36] 1.48 us +- 0.04 us -> [atomicl_py.py36] 1.02 us +- 0.02 us: 1.45x faster (-31%)
    increment: Mean +- std dev: [atomic.py36] 557 ns +- 16 ns -> [atomicl_py.py36] 1.17 us +- 0.02 us: 2.09x slower (+109%)
    decrement: Mean +- std dev: [atomic.py36] 552 ns +- 23 ns -> [atomicl_py.py36] 1.17 us +- 0.02 us: 2.13x slower (+113%)
    setter: Mean +- std dev: [atomic.py36] 1.55 us +- 0.06 us -> [atomicl_py.py36] 463 ns +- 8 ns: 3.34x faster (-70%)
    cas: Mean +- std dev: [atomic.py36] 1.78 us +- 0.04 us -> [atomicl_py.py36] 1.19 us +- 0.02 us: 1.50x faster (-33%)

``Python 3.4.6``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.py34] 1.56 us +- 0.04 us -> [atomicl_cy.py34] 75.2 ns +- 0.7 ns: 20.70x faster (-95%)
    ctor: Mean +- std dev: [atomic.py34] 1.45 us +- 0.03 us -> [atomicl_cy.py34] 92.0 ns +- 1.3 ns: 15.80x faster (-94%)
    increment: Mean +- std dev: [atomic.py34] 518 ns +- 5 ns -> [atomicl_cy.py34] 33.9 ns +- 0.3 ns: 15.30x faster (-93%)
    decrement: Mean +- std dev: [atomic.py34] 530 ns +- 18 ns -> [atomicl_cy.py34] 33.2 ns +- 0.3 ns: 15.96x faster (-94%)
    setter: Mean +- std dev: [atomic.py34] 1.39 us +- 0.04 us -> [atomicl_cy.py34] 44.6 ns +- 1.2 ns: 31.09x faster (-97%)
    cas: Mean +- std dev: [atomic.py34] 1.54 us +- 0.03 us -> [atomicl_cy.py34] 122 ns +- 1 ns: 12.55x faster (-92%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.py34] 1.56 us +- 0.04 us -> [atomicl_py.py34] 995 ns +- 21 ns: 1.56x faster (-36%)
    ctor: Mean +- std dev: [atomic.py34] 1.45 us +- 0.03 us -> [atomicl_py.py34] 941 ns +- 26 ns: 1.55x faster (-35%)
    increment: Mean +- std dev: [atomic.py34] 518 ns +- 5 ns -> [atomicl_py.py34] 1.09 us +- 0.02 us: 2.10x slower (+110%)
    decrement: Mean +- std dev: [atomic.py34] 530 ns +- 18 ns -> [atomicl_py.py34] 1.10 us +- 0.02 us: 2.08x slower (+108%)
    setter: Mean +- std dev: [atomic.py34] 1.39 us +- 0.04 us -> [atomicl_py.py34] 456 ns +- 9 ns: 3.05x faster (-67%)
    cas: Mean +- std dev: [atomic.py34] 1.54 us +- 0.03 us -> [atomicl_py.py34] 1.02 us +- 0.02 us: 1.50x faster (-33%)

``PyPy 5.8.0-beta0``::

    # atomic / atomicl (Cython)
    ctor_default: Mean +- std dev: [atomic.pypy3] 183 ns +- 4 ns -> [atomicl_cy.pypy3] 4.70 us +- 0.13 us: 25.63x slower (+2463%)
    ctor: Mean +- std dev: [atomic.pypy3] 169 ns +- 4 ns -> [atomicl_cy.pypy3] 4.28 us +- 0.11 us: 25.35x slower (+2435%)
    increment: Mean +- std dev: [atomic.pypy3] 27.8 ns +- 0.7 ns -> [atomicl_cy.pypy3] 304 ns +- 8 ns: 10.94x slower (+994%)
    decrement: Mean +- std dev: [atomic.pypy3] 27.7 ns +- 0.2 ns -> [atomicl_cy.pypy3] 303 ns +- 6 ns: 10.93x slower (+993%)
    setter: Mean +- std dev: [atomic.pypy3] 261 ns +- 7 ns -> [atomicl_cy.pypy3] 93.8 ns +- 3.1 ns: 2.78x faster (-64%)
    cas: Mean +- std dev: [atomic.pypy3] 268 ns +- 13 ns -> [atomicl_cy.pypy3] 2.79 us +- 0.18 us: 10.42x slower (+942%)

    # atomic / atomicl (Python)
    ctor_default: Mean +- std dev: [atomic.pypy3] 183 ns +- 4 ns -> [atomicl_py.pypy3] 483 ns +- 32 ns: 2.64x slower (+164%)
    ctor: Mean +- std dev: [atomic.pypy3] 169 ns +- 4 ns -> [atomicl_py.pypy3] 441 ns +- 37 ns: 2.61x slower (+161%)
    increment: Mean +- std dev: [atomic.pypy3] 27.8 ns +- 0.7 ns -> [atomicl_py.pypy3] 282 ns +- 4 ns: 10.15x slower (+915%)
    decrement: Mean +- std dev: [atomic.pypy3] 27.7 ns +- 0.2 ns -> [atomicl_py.pypy3] 286 ns +- 6 ns: 10.33x slower (+933%)
    setter: Mean +- std dev: [atomic.pypy3] 261 ns +- 7 ns -> [atomicl_py.pypy3] 0.23 ns +- 0.00 ns: 1139.07x faster (-100%)
    cas: Mean +- std dev: [atomic.pypy3] 268 ns +- 13 ns -> [atomicl_py.pypy3] 275 ns +- 4 ns: 1.03x slower (+3%)

License
-------
MIT


.. _AtomicLong: https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/atomic/AtomicLong.html
.. _atomic: https://github.com/cyberdelia/atomic
.. _Cython: http://cython.org
.. _CFFI: https://cffi.readthedocs.io
.. _benchmarks.py: https://github.com/gagoman/atomicl/blob/master/benchmarks.py
