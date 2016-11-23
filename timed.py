import time
from collections import namedtuple


def timedcall(fn, *args):
    start = time.clock()
    result = fn(*args)
    end = time.clock()
    nt = namedtuple('Time', 'elapsed result')
    return nt(end - start, result)


def timedcalls(n, fn, *args):
    """Run fn function multiple times.
    If n is an integer call function n times.
    If n is a float repeatedly call function until n seconds pass.
    """
    times = []

    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    elif isinstance(n, float):
        while sum(times) < n:
            elapsed = timedcall(fn, *args)[0]
            times.append(elapsed)

    nt = namedtuple('Time', 'min average max message')
    return nt(min(times), average(times), max(times),
              '{} called {} times in {} seconds.'
              .format(fn.__name__, len(times), sum(times)))


def average(num_collection):
    return sum(num_collection) / len(num_collection)


def foo(n):
    return '-'.join(str(i) for i in range(n))


def main():
    output = timedcall(foo, 100)
    print(output)

    output = timedcalls(10, foo, 100000)
    print(output)

    output = timedcalls(5.0, foo, 100000)
    print(output)


if __name__ == '__main__':
    main()
