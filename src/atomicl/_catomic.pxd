cdef extern from '_atomic.h' nogil:
    ctypedef struct atomic_long_long:
        pass

    void init_atomic_long_long(atomic_long_long *ptr, long long val)
    long long load_value(atomic_long_long *ptr)
    void store_value(atomic_long_long *ptr, long long val)

    long long get_and_add(atomic_long_long *ptr, long long val)
    long long get_and_sub(atomic_long_long *ptr, long long val)
    long long get_and_set(atomic_long_long *ptr, long long val)
    bint compare_and_set(atomic_long_long *ptr, long long exp, long long val)
