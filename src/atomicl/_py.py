import threading

from atomicl import _structure


__all__ = ['AtomicLong']


def raise_on_not_long(msg_format, val):
    if not isinstance(val, int):
        raise ValueError(msg_format % (val,))


class AtomicLong(_structure.AtomicLong):
    __slots__ = ('_lock', '_value')

    def __init__(self, initial_value=0):
        raise_on_not_long('initial value "%s" is not a long', initial_value)

        self._lock = threading.Lock()
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

        self.__get_and_add(other)

        return self

    def __isub__(self, other):
        raise_on_not_long('delta value "%s" is not a long', other)

        self.__get_and_add(-other)

        return self

    def get_and_set(self, new_value):
        raise_on_not_long('new value "%s" is not a long', new_value)

        with self._lock:
            current = self._value
            self._value = new_value
            return current

    def compare_and_set(self, expected_value, new_value):
        raise_on_not_long('expected value "%s" is not a long', expected_value)
        raise_on_not_long('new value "%s" is not a long', new_value)

        with self._lock:
            if self._value != expected_value:
                return False

            self._value = new_value

            return True

    def __get_and_add(self, delta):
        with self._lock:
            current = self._value
            self._value += delta
            return current

    def __repr__(self):
        return '<{0} at 0x{1}: {2!r}>'.format(
            self.__class__.__name__, id(self), self._value)
