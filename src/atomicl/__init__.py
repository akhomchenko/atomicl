try:
    from ._cy import AtomicLong
except ImportError:
    from ._py import AtomicLong


__all__ = ["AtomicLong"]
