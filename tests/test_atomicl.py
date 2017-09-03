import concurrent.futures
import re
import threading

import pytest

from atomicl import _py
from atomicl import _cy


_missing = object()


@pytest.fixture(params=[_py.AtomicLong, _cy.AtomicLong])
def impl(request):
    return request.param


@pytest.mark.parametrize('initial, expected', [
    (_missing, 0),
    (42, 42)
])
def test_initial_default_value(impl, initial, expected):
    counter = impl() if initial is _missing else impl(initial)
    assert counter.value == expected


@pytest.mark.parametrize('initial, val, expected', [
    (0, 5, 5),
    (5, 0, 0)
])
def test_set(impl, initial, val, expected):
    counter = impl(initial)
    counter.value = val
    assert counter.value == expected


@pytest.mark.parametrize('initial, val, expected', [
    (0, 1, 1),
    (0, 5, 5),
    (40, 2, 42)
])
def test_add(impl, initial, val, expected):
    counter = impl(initial)
    counter += val
    assert counter.value == expected


@pytest.mark.parametrize('initial, val, expected', [
    (0, 1, -1),
    (0, 5, -5),
    (44, 2, 42)
])
def test_sub(impl, initial, val, expected):
    counter = impl(initial)
    counter -= val
    assert counter.value == expected


@pytest.mark.parametrize('initial, val', [
    (0, 5),
    (5, 0)
])
def test_get_and_set(impl, initial, val):
    counter = impl(initial)
    assert counter.get_and_set(val) == initial
    assert counter.value == val


@pytest.mark.parametrize('initial, expected_value, val, success', [
    (0, 0, 42, True),
    (0, 42, 2, False)
])
def test_compare_and_set(impl, initial, expected_value, val, success):
    counter = impl(initial)
    assert counter.compare_and_set(expected_value, val) == success
    assert counter.value == (val if success else initial)


@pytest.mark.parametrize('val', [0, 43])
def test_repr(impl, val):
    pattern = re.compile(r'<AtomicLong at 0x\d+: %d>' % val)
    match = re.match(pattern, repr(impl(val)))
    assert bool(match) is True


@pytest.mark.parametrize('val, msg', [
    ('foo', 'new value "foo" is not a long'),
    (1.5, 'new value "1.5" is not a long'),
    ([], 'new value "[]" is not a long')
])
def test_raises_if_new_value_is_not_a_long(impl, val, msg):
    counter = impl()

    with pytest.raises(ValueError) as exc_info:
        counter.value = val

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('val, msg', [
    ('foo', 'initial value "foo" is not a long'),
    (1.5, 'initial value "1.5" is not a long'),
    ([], 'initial value "[]" is not a long')
])
def test_raises_if_initial_value_is_not_a_long(impl, val, msg):
    # raises#match behaves weirdly with []
    with pytest.raises(ValueError) as exc_info:
        impl(val)

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('op', [
    '__iadd__',
    '__isub__'
])
@pytest.mark.parametrize('val, msg', [
    (1.5, 'delta value "1.5" is not a long'),
    ('foo', 'delta value "foo" is not a long'),
    ([], 'delta value "[]" is not a long')
])
def test_raises_if_value_for_i_op_is_not_a_long(impl, op, val, msg):
    counter = impl()
    method = getattr(counter, op)

    with pytest.raises(ValueError) as exc_info:
        method(val)

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('val, msg', [
    (1.5, 'new value "1.5" is not a long'),
    ('foo', 'new value "foo" is not a long'),
    ([], 'new value "[]" is not a long')
])
def test_raises_if_value_for_get_and_set_is_not_a_long(impl, val, msg):
    counter = impl()

    with pytest.raises(ValueError) as exc_info:
        counter.get_and_set(val)

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('val, msg', [
    (1.5, 'expected value "1.5" is not a long'),
    ('foo', 'expected value "foo" is not a long'),
    ([], 'expected value "[]" is not a long')
])
def test_raises_if_expected_value_for_cas_is_not_a_long(impl, val, msg):
    counter = impl()

    with pytest.raises(ValueError) as exc_info:
        counter.compare_and_set(val, 1)

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('val, msg', [
    (1.5, 'new value "1.5" is not a long'),
    ('foo', 'new value "foo" is not a long'),
    ([], 'new value "[]" is not a long')
])
def test_raises_if_new_value_for_cas_if_not_a_long(impl, val, msg):
    counter = impl()

    with pytest.raises(ValueError) as exc_info:
        counter.compare_and_set(1, val)

    assert str(exc_info.value) == msg


@pytest.mark.parametrize('op, loops, val, expected', [
    ('__iadd__', 10 ** 5, 1, 200000),
    ('__isub__', 10 ** 5, 1, -200000)
])
def test_concurrently(impl, op, loops, val, expected):
    def worker():
        nonlocal counter, event

        method = getattr(counter, op)

        event.wait()

        for _ in range(loops):
            method(val)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for _ in range(2 ** 5):
            counter = impl()
            event = threading.Event()

            fs = [pool.submit(worker) for _ in range(2)]

            event.set()

            concurrent.futures.wait(fs)

            assert counter.value == expected
