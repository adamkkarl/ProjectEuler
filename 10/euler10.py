#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all primes less than or equal to N"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler010/copy-from/1306804366
#First line T is number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 1000; 1 <= N <= 10**6

import sys
from math import sqrt


def sieve():
    """fills isPrime array with booleans for whether the number at isPrime[i] is prime or not"""
    """uses a process known as the sieve of eratosthenes"""
    isPrime = [True] * 1000001 #for numbers from 0 to 100000 inclusive
    #print(isPrime)
    isPrime[0] = False
    isPrime[1] = False
    index = 2
    while index <= 1000000:
        if isPrime[index]: #found a prime number
            multiplier = 2
            while index * multiplier <= 1000000:
                isPrime[index*multiplier] = False #all multiples of the prime are not prime
                multiplier += 1
        index += 1
    return isPrime
    
def generate_list_of_sums(isPrime):
    """given a list of 100 000 booleans on whether an index is prime or not,
    return a list of 100 000 sums of all primes <= index"""
    sums = [0] * 1000001
    for index in range(1,1000001):
        new_sum = sums[index-1]
        if isPrime[index]:
            new_sum += index
        sums[index] = new_sum
    return sums


def main():
    isPrime = sieve() #generate isPrime
    listOfSums = generate_list_of_sums(isPrime)
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())

        print(str(listOfSums[n]))

if __name__ == "__main__":
    main()
