
import math
import time


def eratosthens_sieve(n):
    """The Sieve of Eratosthenes
    Return list of prime numbers up to n.
    
    """
    primality = [True] * (n+1)
    primality[0] = False
    primality[1] = False
    limit = math.floor(math.sqrt(n))

    for index in range(2, limit+1):
        if primality[index]:
            for multiple in range(index*index, n+1, index):
                primality[multiple] = False

    return [index
            for index, isprime in enumerate(primality)
            if isprime is True]


def is_prime(nr):
    if nr <= 1:
        return False
    if nr % 2 == 0:
        return False
    limit = math.floor(math.sqrt(nr))

    for candidate in range(3, limit+1, 2):
        if nr % candidate == 0:
            return False
    return True


def naive_primes_up_tp(n):
    primes = [2]
    for nr in range(3, n+1, 2):
        if is_prime(nr):
            primes.append(nr)

    return primes


def compare_execution_times(n):
    print('Find all prime numbers up to {:,d}'.format(n))

    start_time = time.perf_counter()
    primes = eratosthens_sieve(n)
    elapsed_time = time.perf_counter() - start_time
    print('Eratosthenes sieve duration: {:.3f} seconds'.format(elapsed_time))

    start_time = time.perf_counter()
    primes = naive_primes_up_tp(n)
    elapsed_time = time.perf_counter() - start_time
    print('Naive approach duration: {:.3f} seconds'.format(elapsed_time))



def main():
    upto = 10**2

    print('Eratosthenes sieve')
    print('List of primes up to {:,d}'.format(upto))
    start_time = time.perf_counter()
    primes = eratosthens_sieve(upto)
    elapsed_time = time.perf_counter() - start_time

    print(primes)
    print('{} primes found in {:.3f} seconds.'.format(len(primes), elapsed_time))

    print()
    compare_execution_times(10**6)


if __name__ == '__main__':
    main()
