#ifndef ATOMICL__ATOMIC_H_
#define ATOMICL__ATOMIC_H_

#include <stdatomic.h>

typedef struct atomic_long_long {
    _Atomic long long value;
} atomic_long_long;

void init_atomic_long_long(atomic_long_long *ptr, long long val);
long long load_value(atomic_long_long *ptr);
void store_value(atomic_long_long *ptr, long long val);

long long get_and_add(atomic_long_long *ptr, long long val);
long long get_and_sub(atomic_long_long *ptr, long long val);
long long get_and_set(atomic_long_long *ptr, long long val);
int compare_and_set(atomic_long_long *ptr, long long exp, long long val);

#endif  // ATOMICL__ATOMIC_H_
