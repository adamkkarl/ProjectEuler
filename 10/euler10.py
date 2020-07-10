#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all primes less than or equal to N"""
#https://projecteuler.net/problem=10

from math import sqrt

isPrime = []

def sieve(n):
    """fills isPrime array with booleans for whether the number at isPrime[i] is prime or not"""
    """uses a process known as the sieve of eratosthenes"""
    global isPrime
    isPrime = [True for i in range(n+1)] #for numbers from 0 to n inclusive
    isPrime[0] = False
    isPrime[1] = False
    index = 2
    while index <= n:
        if isPrime[index]: #found a prime number
            multiplier = 2
            while index * multiplier <= n:
                isPrime[index * multiplier] = False #all multiples of the prime are not prime
                multiplier += 1
        index += 1
    return isPrime

def sumPrimes(n):
    """given a list of n booleans on whether an index is prime or not,
    return the sum of all primes <= index"""
    s = 0
    for index in range(1, n+1):
        if isPrime[index]:
            s += index
    return s

def main():
    print("Find the sum of all primes below: ", end="")
    n = int(input().strip())
    isPrime = sieve(n) #generate isPrime
    print("Sum = %d" % sumPrimes(n))

if __name__ == "__main__":
    main()
