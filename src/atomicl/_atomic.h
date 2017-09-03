#ifndef ATOMICL__ATOMIC_H_
#define ATOMICL__ATOMIC_H_

long long get_and_add(long long *ptr, long long val);
long long get_and_sub(long long *ptr, long long val);
long long get_and_set(long long *ptr, long long val);
int compare_and_set(long long *ptr, long long exp, long long val);

#endif  // ATOMICL__ATOMIC_H_
