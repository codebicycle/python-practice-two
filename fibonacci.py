import functools

@functools.lru_cache(maxsize=None)
def fibonacci_one(n):
    """Fibonacci lru_cache decorator"""
    if n < 2:
        return n
    return fibonacci_one(n-1) + fibonacci_one(n-2)


def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_two(n):
    """Fibonacci memoize decorator"""
    if n < 2:
        return n
    return fibonacci_two(n-1) + fibonacci_two(n-2)


def fibonacci_three(n, cache={}):
    """Fibonacci mutable default argument cache"""
    if n < 2:
        return n

    if n in cache:
        return cache[n]

    prev = cache.get(n-1, fibonacci_three(n-1))
    preprev = cache.get(n-2, fibonacci_three(n-2))
    cache[n] = prev + preprev
    return cache[n]
