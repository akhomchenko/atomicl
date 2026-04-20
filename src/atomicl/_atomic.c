#include "_atomic.h"

void init_atomic_long_long(atomic_long_long* ptr, long long val) {
    atomic_init(&ptr->value, val);
}

long long load_value(atomic_long_long* ptr) {
    return atomic_load(&ptr->value);
}

void store_value(atomic_long_long* ptr, long long val) {
    atomic_store(&ptr->value, val);
}

long long get_and_add(atomic_long_long* ptr, long long val) {
    return atomic_fetch_add(&ptr->value, val);
}

long long get_and_sub(atomic_long_long* ptr, long long val) {
    return atomic_fetch_sub(&ptr->value, val);
}

long long get_and_set(atomic_long_long* ptr, long long val) {
    return atomic_exchange(&ptr->value, val);
}

int compare_and_set(atomic_long_long* ptr, long long exp, long long val) {
    return atomic_compare_exchange_strong(&ptr->value, &exp, val);
}
