#!/bin/python3

__author__ = "Adam Karl"
"""Find the difference between the sum of the squares of the first N natural numbers and the square of the sum"""
#https://projecteuler.net/problem=6
#Constraints: 1 <= T <= 10**4; 1 <= N <= 10**4

import sys
from math import sqrt

def sum_of_ints(n):
    """Return the sum of 1 to n"""
    return ((n + 1) * n) >> 1

def sum_of_squares(n):
    """Return the sum of (1 to n) squared"""
    return n * (n + 1) * ((2 * n) + 1) // 6

def main():
    print("Find the difference between sum of squares and square of sum from 1 to: ", end="")
    n = int(input().strip())
    
    a = sum_of_ints(n) ** 2
    b = sum_of_squares(n)
    print("Difference: %d" %(a - b))

if __name__ == "__main__":
    main()
