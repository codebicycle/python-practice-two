import math

def first_prime_factor(number):
        if number % 2 == 0:
            return 2

        limit = math.ceil(math.sqrt(number))
        for i in range(3, limit + 1, 2):
            if number % i == 0:
                return i

        return number

def factorize_primes(number):
    factors = []
    while number > 1:
        factor = first_prime_factor(number)
        factors.append(factor)
        number //= factor
    return factors


def main():
    for num in range(101):
        prime_factors = factorize_primes(num)
        prime_factors_str = ', '.join(map(str, prime_factors))
        print('{:>3}: {}'.format(num, prime_factors_str))


if __name__ == '__main__':
     main()
