
def add(first, second):
    return first + second

def add_to(first):
    def adder(second):
        return add(first, second)
    return adder

def tracer(f):
    def inner(*args):
        print("Calling {}{!r}".
                format(f, args))
        result = f(*args)
        print('Returning', result)
        return result
    return inner


def main_a():
    res = add(1, 2)
    print('add(1, 2) ->', res)

    add_to_2 = add_to(2)
    res = add_to_2(3)
    print('add_to_2(3) ->', res)


def main_b():
    add_trace = tracer(add)
    res = add_trace(4, 4)
    print('add_trace(4, 4) ->', res)


def main_c():
    def add(first, second):
        return first + second

    print('Overwrite add function.')
    add = tracer(add)

    res = add(5, 5)
    print('add(5, 5) ->', res)


def main_d():
    @tracer
    def add(first, second):
        return first + second

    res = add(8, 8)
    print('add(8, 8) ->', res)


def main():
    main_a()
    main_b()
    main_c()
    main_d()


if __name__ == '__main__':
    main()
