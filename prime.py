# Find first n prime numbers and print them

from math import ceil, sqrt

def isPrime(a):
    if a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3,ceil(sqrt(a)) + 1,2):
            if a % i == 0:
                return False
        return True

def print_n_primes(a):
    i = 0
    m = 2
    while True:
        if isPrime(m) ==True:
            print(m)
            i += 1
        m += 1
        if i == a:
            break