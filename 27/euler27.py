#!/bin/python3

__author__ = "Adam Karl"
"""Find the coefficients a and b to n**2 + an + b that produce the maximum number of primes for n=0,1,2,... such that abs(a) and abs(b) <= N"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler027/problem
#First line contains integer N
#Constraints: 42 <= N <= 2000

primesMemo = []

def isPrime(test):
    """Return True if test input is prime, False otherwise"""
    """Has an error if we didnt generate enough primes"""
    if primesMemo[test] == 1:
        return True
    return False

def findPrimesInSeq(a, b):
    """Given a and b, return the primes in sequence n**2 + an + b"""
    """Since N >= 42, if a and b < 41 we can disregard since a=-1 and b=41 returns 42 primes"""
    if a < 41 and b < 41:
        return 0
    
    n = 0
    while isPrime(pow(n,2) + n * a + b):
        n += 1
    return n

def generatePrimes(max_prime):
    """Find and return an array of 1s and 0s such that arr[n] has a 1 iff n is prime"""
    testPrimes = [1] * (max_prime + 1) #1 found in testPrimes[n] if n is prime, 0 if not prime
    testPrimes[0] = 0 #0 not prime
    testPrimes[1] = 0 #1 not prime
    
    index = 2
    while index < max_prime + 1:
        if testPrimes[index] == 1:#found a prime
            multiple = index * 2
            while multiple <= max_prime: #zero out all multiples
                testPrimes[multiple] = 0
                multiple += index
        index += 1
    return testPrimes

def findPossibleBValues(N):
    """Return a list of of values for B such that B is positive, prime, and abs(A) <= N"""
    arr = generatePrimes(N)
    
    length = len(arr)
    bValues = []
    
    i = 0
    while i < length:
        if arr[i] == 1: #i is prime
            bValues.append(i)
        i += 1
    return bValues
        

def findPossibleAValues(N):
    """Return a list of of values for A such that A is odd and abs(A) <= N"""
    if N % 2 == 0:
        N -=1
    aValues = []
    values = list(range(1, N+1, 2))
    for item in values[::-1]:
        aValues.append(-1 * item)
    for item in values:
        aValues.append(item)
    return aValues
        

def calculateMaxPrimes(N):
    """Given 42 <= N <= 2000, compute a and b for which n**2 + an + b produces the maximum number of primes
    for consecutive n values starting at n=0, n=1, ....
    a and b have a magnitude <= N"""
    #NOTES
    #b must be a positive prime number for n=0 case
    #a must be odd for n=1 case to be odd
    maxA = 0
    maxB = 0
    maxNumPrimes = 0
    
    aValues = findPossibleAValues(N)
    bValues = findPossibleBValues(N)
    
    for b in bValues:
        for a in aValues:
            test = findPrimesInSeq(a, b)
            if test > maxNumPrimes:
                maxA = a
                maxB = b
                maxNumPrimes = test
    return maxA, maxB


def main():
    global primesMemo
    primesMemo = generatePrimes(50000)
    N = int(input())
    
    resultA, resultB = calculateMaxPrimes(N)
    print(resultA, end=" ")
    print(resultB)

if __name__ == "__main__":
    main()
