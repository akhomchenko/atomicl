cdef extern from '_atomic.h' nogil:
    long long get_and_add(long long *ptr, long long val)
    long long get_and_sub(long long *ptr, long long val)
    long long get_and_set(long long *ptr, long long val)
    bint compare_and_set(long long *ptr, long long exp, long long val)
