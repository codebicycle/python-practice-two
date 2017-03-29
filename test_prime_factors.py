from prime_factors import factorize_primes

def test_factorize_primes():
    assert [] == factorize_primes(0)
    assert [] == factorize_primes(1)
    assert [2] == factorize_primes(2)
    assert [3] == factorize_primes(3)
    assert [2, 2] == factorize_primes(4)
    assert [5] == factorize_primes(5)
    assert [2, 3] == factorize_primes(6)
    assert [7] == factorize_primes(7)
    assert [2, 2, 2] == factorize_primes(8)
    assert [3, 3] == factorize_primes(9)

    assert [] == factorize_primes(-1)
    assert [] == factorize_primes(-2)
    assert [] == factorize_primes(-3)
    assert [] == factorize_primes(-100)

    assert [3, 5, 7] == factorize_primes(105)
    assert [2, 2, 5, 5] == factorize_primes(100)