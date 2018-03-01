import argparse
from itertools import count, chain
from math import sqrt


def is_prime(n):
    """
    Returns True if n is prime and False otherwise.
    """
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes(stop=None):
    """
    Return a generator of prime numbers from 2 to infinity
    or to stop (excluding) if stop is defined.
    """
    if stop is None:
        high_primes = ((p for p in count(start=3, step=2) if is_prime(p)))
    else:
        high_primes = ((p for p in range(3, stop+1, 2) if is_prime(p)))
    return chain([2], high_primes)


def list_primes(stop=None):
    """
        Return a list of prime numbers from 2 to infinity
        or to stop (excluding) if stop is defined.
    """
    return list(primes(stop))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('stop', type=int, default=None)
    parser.description = "list all prime numbers no more than stop " + \
                         "or to infinity if stop is omitted."
    a = parser.parse_args()
    print(*primes(a.stop))


if __name__ == '__main__':
    main()
