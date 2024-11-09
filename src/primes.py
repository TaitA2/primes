"""
Python Library for quality of life functions relating to prime numbers
"""


"""Helper function for generating prime numbers"""
def __findPrimes(condition):
    primes = []
    i = 2

    while condition(primes, i):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1

    return primes



"""Returns a list of the first n primes"""
def nPrimes(n):
    return findPrimes(lambda primes, i: len(primes) < n)



"""Returns a list of primes less than n"""
def primesBelowN(n):
    return findPrimes(lambda primes, i: i < n)



"""Returns nth prime"""
def nthPrime(n):
    return nPrimes()[-1]



"""Returns True if n is prime else False"""
def isPrime(n):
    for p in __findPrimes(lambda primes, i: i < n ** 0.5):
        if n % p == 0:
            return False
    return True
