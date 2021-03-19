import time
from functools import lru_cache


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n-2)


@lru_cache
def fibLru(n):
    if n < 2:
        return n
    return fibLru(n - 1) + fibLru(n-2)


def fibCache(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    if n <= 1:
        return n

    cache[n] = fibCache(n - 1, cache=cache) + fibCache(n-2, cache=cache)

    return cache[n]


n = 30
start = time.perf_counter()
print(fib(n))
end = time.perf_counter()
print("Unoptimized Recursive Function")
print("Time Taken:", "{:.7f}".format(end-start))

start = time.perf_counter()
print(fibLru(n))
end = time.perf_counter()
print("Optimized Recursive Function")
print("Time Taken:", "{:.7f}".format(end-start))

start = time.perf_counter()
print(fibCache(n))
end = time.perf_counter()
print("Cached Recursive Function")
print("Time Taken:", "{:.7f}".format(end-start))
