#!/bin/python3

__author__ = "Adam Karl"
"""Find the difference between the sum of the squares of the first N natural numbers and the square of the sum"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler006/submissions/code/1306791519
#First line is T the number of test cases, followed by T lines with values of N
#Constraints: 1 <= T <= 10**4; 1 <= N <= 10**4

import sys
from math import sqrt

def sum_of_ints(n):
    return ((n + 1) * n) >> 1

def sum_of_squares(n):
    return n * (n + 1) * ((2 * n) + 1) // 6

def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        
        a = sum_of_ints(n) ** 2
        b = sum_of_squares(n)
        print(a - b)

if __name__ == "__main__":
    main()
