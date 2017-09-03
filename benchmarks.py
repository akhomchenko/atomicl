import perf
import atomic
import atomicl._cy
import atomicl._py


def ctor_default(cls):
    return cls()


def ctor(cls):
    return cls(42)


def inc(counter):
    counter += 1
    return counter


def dec(counter):
    counter -= 1
    return counter


def setter(counter):
    counter.value = 42
    return counter


def cas(counter, expected, val):
    return counter.compare_and_set(expected, val)


if __name__ == '__main__':
    runner = perf.Runner()

    runner.bench_func('atomic#ctor_default', ctor_default, atomic.AtomicLong)
    runner.bench_func('atomicl.py#ctor_default', ctor_default, atomicl._py.AtomicLong)  # noqa: E501
    runner.bench_func('atomicl.cy#ctor_default', ctor_default, atomicl._cy.AtomicLong)  # noqa: E501

    runner.bench_func('atomic#ctor', ctor, atomic.AtomicLong)
    runner.bench_func('atomicl.py#ctor', ctor, atomicl._py.AtomicLong)
    runner.bench_func('atomicl.cy#ctor', ctor, atomicl._cy.AtomicLong)

    runner.bench_func('atomic#increment', inc, atomic.AtomicLong())
    runner.bench_func('atomicl.py#increment', inc, atomicl._py.AtomicLong())
    runner.bench_func('atomicl.cy#increment', inc, atomicl._cy.AtomicLong())

    runner.bench_func('atomic#decrement', dec, atomic.AtomicLong())
    runner.bench_func('atomicl.py#decrement', dec, atomicl._py.AtomicLong())
    runner.bench_func('atomicl.cy#decrement', dec, atomicl._cy.AtomicLong())

    runner.bench_func('atomic#setter', setter, atomic.AtomicLong())
    runner.bench_func('atomicl.py#setter', setter, atomicl._py.AtomicLong())
    runner.bench_func('atomicl.cy#setter', setter, atomicl._cy.AtomicLong())

    runner.bench_func('atomic#cas', cas, atomic.AtomicLong(0), 0, 42)
    runner.bench_func('atomicl.py#cas', cas, atomicl._py.AtomicLong(0), 0, 42)
    runner.bench_func('atomicl.cy#cas', cas, atomicl._cy.AtomicLong(0), 0, 42)
