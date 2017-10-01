import functools

import atomic
import perf

import atomicl._cy
import atomicl._py


IMPLEMENTATIONS = {
    'atomic': atomic.AtomicLong,
    'atomicl_py': atomicl._py.AtomicLong,
    'atomicl_cy': atomicl._cy.AtomicLong
}


def benchmark_name(name, ctx, prefix=None, use_prefix=False):
    if use_prefix:
        return '%s%s' % (prefix % ctx, name)

    return name


def add_cmdline_args(cmd, args):
    if args.impl:
        cmd.extend(['--impl', args.impl])


def ctor_default(loops, cls):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()
        cls()

    return perf.perf_counter() - t0


def ctor(loops, cls):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)
        cls(42)

    return perf.perf_counter() - t0


def inc(loops, counter):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1
        counter += 1

    return perf.perf_counter() - t0


def dec(loops, counter):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1
        counter -= 1

    return perf.perf_counter() - t0


def setter(loops, counter):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42
        counter.value = 42

    return perf.perf_counter() - t0


def cas(loops, counter, first, second):
    range_it = range(loops)
    t0 = perf.perf_counter()

    for _ in range_it:
        counter.compare_and_set(first, second)
        counter.compare_and_set(second, first)
        counter.compare_and_set(first, second)
        counter.compare_and_set(second, first)
        counter.compare_and_set(first, second)
        counter.compare_and_set(second, first)
        counter.compare_and_set(first, second)
        counter.compare_and_set(second, first)
        counter.compare_and_set(first, second)
        counter.compare_and_set(second, first)

    return perf.perf_counter() - t0


if __name__ == '__main__':
    runner = perf.Runner(add_cmdline_args=add_cmdline_args)

    parser = runner.argparser
    parser.add_argument('--impl', choices=sorted(IMPLEMENTATIONS),
                        help='specific implementation to benchmark')

    options = parser.parse_args()
    implementations = (options.impl,) if options.impl else IMPLEMENTATIONS

    for impl in implementations:
        impl = IMPLEMENTATIONS[impl]
        name = functools.partial(benchmark_name, ctx=dict(impl=impl),
                                 prefix='(impl = %(impl)s) ',
                                 use_prefix=len(implementations) > 1)

        runner.bench_time_func(name('ctor_default'),
                               ctor_default, impl,
                               inner_loops=10)
        runner.bench_time_func(name('ctor'),
                               ctor, impl,
                               inner_loops=10)
        runner.bench_time_func(name('increment'),
                               inc, impl(),
                               inner_loops=10)
        runner.bench_time_func(name('decrement'),
                               dec, impl(),
                               inner_loops=10)
        runner.bench_time_func(name('setter'),
                               setter, impl(),
                               inner_loops=10)
        runner.bench_time_func(name('cas'),
                               cas, impl(0), 0, 42,
                               inner_loops=10)
