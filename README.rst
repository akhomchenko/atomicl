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

    atomic#ctor_default: Mean +- std dev: 1.64 us +- 0.05 us
    atomicl.py#ctor_default: Mean +- std dev: 1.13 us +- 0.02 us
    atomicl.cy#ctor_default: Mean +- std dev: 260 ns +- 10 ns
    atomic#ctor: Mean +- std dev: 1.65 us +- 0.03 us
    atomicl.py#ctor: Mean +- std dev: 1.17 us +- 0.03 us
    atomicl.cy#ctor: Mean +- std dev: 286 ns +- 4 ns
    atomic#increment: Mean +- std dev: 740 ns +- 16 ns
    atomicl.py#increment: Mean +- std dev: 1.34 us +- 0.02 us
    atomicl.cy#increment: Mean +- std dev: 210 ns +- 3 ns
    atomic#decrement: Mean +- std dev: 734 ns +- 23 ns
    atomicl.py#decrement: Mean +- std dev: 1.36 us +- 0.02 us
    atomicl.cy#decrement: Mean +- std dev: 209 ns +- 5 ns
    atomic#setter: Mean +- std dev: 1.79 us +- 0.04 us
    atomicl.py#setter: Mean +- std dev: 653 ns +- 14 ns
    atomicl.cy#setter: Mean +- std dev: 223 ns +- 3 ns
    atomic#cas: Mean +- std dev: 1.99 us +- 0.05 us
    atomicl.py#cas: Mean +- std dev: 1.33 us +- 0.02 us
    atomicl.cy#cas: Mean +- std dev: 318 ns +- 3 ns

``Python 3.4.6``::

    atomic#ctor_default: Mean +- std dev: 1.81 us +- 0.04 us
    atomicl.py#ctor_default: Mean +- std dev: 1.29 us +- 0.02 us
    atomicl.cy#ctor_default: Mean +- std dev: 377 ns +- 12 ns
    atomic#ctor: Mean +- std dev: 1.88 us +- 0.07 us
    atomicl.py#ctor: Mean +- std dev: 1.32 us +- 0.02 us
    atomicl.cy#ctor: Mean +- std dev: 403 ns +- 7 ns
    atomic#increment: Mean +- std dev: 862 ns +- 26 ns
    atomicl.py#increment: Mean +- std dev: 1.48 us +- 0.04 us
    atomicl.cy#increment: Mean +- std dev: 353 ns +- 7 ns
    atomic#decrement: Mean +- std dev: 865 ns +- 22 ns
    atomicl.py#decrement: Mean +- std dev: 1.47 us +- 0.02 us
    atomicl.cy#decrement: Mean +- std dev: 353 ns +- 5 ns
    atomic#setter: Mean +- std dev: 1.84 us +- 0.05 us
    atomicl.py#setter: Mean +- std dev: 796 ns +- 23 ns
    atomicl.cy#setter: Mean +- std dev: 368 ns +- 3 ns
    atomic#cas: Mean +- std dev: 1.96 us +- 0.05 us
    atomicl.py#cas: Mean +- std dev: 1.34 us +- 0.03 us
    atomicl.cy#cas: Mean +- std dev: 448 ns +- 17 ns

License
-------
MIT


.. _AtomicLong: https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/atomic/AtomicLong.html
.. _atomic: https://github.com/cyberdelia/atomic
.. _Cython: http://cython.org
.. _CFFI: https://cffi.readthedocs.io
.. _benchmarks.py: https://github.com/gagoman/atomicl/blob/master/benchmarks.py
