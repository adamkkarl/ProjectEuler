#!/bin/python3

__author__ = "Adam Karl"
"""Find the largest prime factor of given number N"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem
#Solved April 2018

import sys
from math import sqrt

    
def largestFactor(n):
    """Given integer N, return its largest prime factor"""
    largest = 1
    
    while n % 2 == 0:
        largest = 2
        n = n >> 1
        
    divisor = 3
    while n > 1 and divisor <= sqrt(n):
        if n % divisor == 0: #found a factor
            if divisor > largest:
                largest = divisor
            n = int(round(n / divisor))
            divisor = 3 #reset
        else:
            divisor += 2 #only need to check odd divisors >= 3
    if n > 1 and n > largest:
        largest = int(round(n))
    return largest

def main():
    print("Enter number to find largest prime factor of: ", end="")
    n = int(input().strip())
    print("%d's largest prime factor is %d" % (n,largestFactor(n)))

if __name__ == "__main__":
    main()
