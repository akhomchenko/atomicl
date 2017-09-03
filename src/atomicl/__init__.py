try:
    from atomicl import _cy
    AtomicLong = _cy.AtomicLong
except ImportError:
    from atomicl import _py
    AtomicLong = _py.AtomicLong


__all__ = ['AtomicLong']
