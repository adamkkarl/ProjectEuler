#!/bin/python3

__author__ = "Adam Karl"
"""Find the smallest value d < N such that 1/d contains the longest recurring cycle in its decimal"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler026/problem
#first line T number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 1000; 4 <= N <= 10 000 

from math import floor

MAXIMUM = 10000 #magic number from problem description
primes = []
longestCycle = [0] * (MAXIMUM + 1)

def generatePrimes(maximum_prime):
    """Generate a list of prime numbers up to and including maximum_prime (input)"""
    testPrimes = [1] * (maximum_prime + 1)
    for i in range(2, maximum_prime + 1): #start at 2 since 0 and 1 not prime
        if testPrimes[i] == 1: #found a prime
            my_prime = i
            primes.append(my_prime) #save prime number
            while my_prime <= MAXIMUM: #all multiples of this prime are not prime
                testPrimes[my_prime] = 0
                my_prime += i  

def generateCycles(maximum_divisor):
    """Generate a list where longestCycles[n] contains the length of the cycle with the longest period
    for 1/i for i <= n"""
    
    primeIndex = 0
    nextPrime = primes[primeIndex]
    
    longestCyclePeriod = 0
    longestCycleValue = 0

    i = 1
    while i <= maximum_divisor:
        while i < nextPrime:
            longestCycle[i] = longestCycle[i-1]
            i += 1
            if i > maximum_divisor:
                break
        #i == nextPrime when we get here
        my_period = findCyclePeriod(i)
        if longestCyclePeriod < my_period: #if new cycle has the longest period so far
            longestCycle[i] = i
            longestCyclePeriod = my_period
        else: #new cycle is too short
            longestCycle[i] = longestCycle[i-1]
                
        primeIndex += 1
        if primeIndex < len(primes):
            nextPrime = primes[primeIndex]
        else:
            break
        i += 1
        
    while i <= maximum_divisor: #just copy index of longest period until end of array
        longestCycle[i] = longestCycle[i-1]
        i += 1
            
def findCyclePeriod(p):
    """Given prime number p, find the period of the cycle for 1/p"""
    if p == 2 or p == 5:
        return 0
    period = 2
    while True:
        if pow(10, period - 1, p) == 1:
            return period - 1
        period += 1

def main():
    generatePrimes(MAXIMUM)
    generateCycles(MAXIMUM)
    t = int(input())
    for a0 in range(t):
        n = int(input())
        print(longestCycle[n-1])#-1 since we want d < N
        
if __name__ == "__main__":
    main()
