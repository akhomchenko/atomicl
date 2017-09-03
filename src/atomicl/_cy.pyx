from atomicl cimport _catomic as atomic
from atomicl import _structure


__all__ = ['AtomicLong']


cdef raise_on_not_long(msg_format, val):
    if not isinstance(val, int):
        raise ValueError(msg_format % (val,))


cdef class AtomicLong:
    cdef long long _value

    def __init__(self, initial_value=0):
        raise_on_not_long('initial value "%s" is not a long', initial_value)

        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        raise_on_not_long('new value "%s" is not a long', new_value)

        self._value = new_value

    def __iadd__(self, other):
        raise_on_not_long('delta value "%s" is not a long', other)

        atomic.get_and_add(&self._value, other)

        return self

    def __isub__(self, other):
        raise_on_not_long('delta value "%s" is not a long', other)

        atomic.get_and_sub(&self._value, other)

        return self

    def get_and_set(self, new_value):
        raise_on_not_long('new value "%s" is not a long', new_value)

        return atomic.get_and_set(&self._value, new_value)

    def compare_and_set(self, expected_value, new_value):
        raise_on_not_long('expected value "%s" is not a long', expected_value)
        raise_on_not_long('new value "%s" is not a long', new_value)

        return atomic.compare_and_set(&self._value, expected_value, new_value)

    def __repr__(self):
        return '<{0} at 0x{1}: {2!r}>'.format(
            self.__class__.__name__, id(self), self._value)


_structure.AtomicLong.register(AtomicLong)
