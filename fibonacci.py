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
    cache[n] = fibonacci_three(n-1, cache) + fibonacci_three(n-2, cache)
    return cache[n]


memo = {}
def fibonacci(n):
    """Recursive dynamic programming algorithm"""
    if n in memo:
        return memo[n]
    if n < 2:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    memo[n] = result
    return result

fib = {}
def fibonacci_four(n):
    """Bottom-up dynamic programming algorithm"""
    for k in range(n+1):
        if k < 2:
            result = k
        else:
            result = fib[k-1] + fib[k-2]
        fib[k] = result
    return fib[n]
