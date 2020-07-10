#!/bin/python3

__author__ = "Adam Karl"
"""What is the Nth prime number"""
#https://projecteuler.net/problem=7
#April 2018

import sys
from math import sqrt

primes = [2,3]

def isPrime(n):
    """could be improved by only testing primes up to the sqrt, not just all integers >=2"""
    if n % 2 == 0:
        return False
    temp = 3
    maximum = round(sqrt(n)) + 1
    while temp < maximum:
        if n % temp == 0:
            return False
        temp += 2
    return True


def main():
    print("Find the Nth prime number. N = ", end="")
    n = int(input().strip())
    if n <= len(primes):
        print(str(primes[n-1]))
    else:
        testPrime = primes[-1] + 2
        while n != len(primes):
            if isPrime(testPrime):
                primes.append(testPrime)
            testPrime += 2
        print(str(primes[n-1]))

if __name__ == "__main__":
    main()
