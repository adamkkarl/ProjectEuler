#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all truncatable primes below N that are truncatable primes from left to right and right to left"""
#https://projecteuler.net/problem=37

isPrime = []

def generatePrimes(n):
    """given n, fill isPrime with boolean values such that isPrime[i] = True if i is prime, False otherwise for values from 0 to n-1"""
    global isPrime
    isPrime = [True for i in range(n)]
    isPrime[0] = False
    isPrime[1] = False
    i = 0
    while i < n:
        if isPrime[i]:
            k = 2 * i
            while k < n:
                isPrime[k] = False
                k += i
        i += 1

def sumTruncPrimes(n):
    """Given int n, return the sum of the integers less than n that are both truncatable from the left and right"""
    truncPrimeSum = 0
    for i in range(10, n):
        if isPrime[i]:
            check_list = []
            s = str(i)
            left = s[:-1]
            while len(left) > 0:
                check_list.append(left)
                left = left[:-1]
            right = s[1:]
            while len(right) > 0:
               check_list.append(right)
               right = right[1:]
            allPrime = True
            for a in check_list:
                if not isPrime[int(a)]:
                    allPrime = False
            if allPrime:
                truncPrimeSum += i
    return truncPrimeSum


def main():
    print("Finding the sum of all 11 truncatable primes")
    max = 1000000
    generatePrimes(max)
    result = sumTruncPrimes(max)
    print("Sum = %d" % result)

if __name__ == "__main__":
    main()
