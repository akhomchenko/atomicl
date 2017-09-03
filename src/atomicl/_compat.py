import abc
import sys


PY34 = sys.version_info >= (3, 4)


if PY34:
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (object,), dict(__slots__=()))


__all__ = ['ABC']
