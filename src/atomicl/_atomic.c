long long get_and_add(long long* ptr, long long val) {
    return __atomic_fetch_add(ptr, val, __ATOMIC_SEQ_CST);
}

long long get_and_sub(long long* ptr, long long val) {
    return __atomic_fetch_sub(ptr, val, __ATOMIC_SEQ_CST);
}

long long get_and_set(long long* ptr, long long val) {
    return __atomic_exchange_n(ptr, val, __ATOMIC_SEQ_CST);
}

int compare_and_set(long long* ptr, long long exp, long long val) {
    return __atomic_compare_exchange_n(ptr, &exp, val, 0, __ATOMIC_SEQ_CST, __ATOMIC_SEQ_CST);
}
