#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all truncatable primes below N that are truncatable primes from left to right and right to left"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler037
#Input: N
#Constraints: 100 <= N <= 10**6

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
    """Given ints n, return the sum of the integers less than n that are both truncatable from the left and right"""
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
    n = int(input())
    generatePrimes(n)
    result = sumTruncPrimes(n)
    print(result)

if __name__ == "__main__":
    main()
