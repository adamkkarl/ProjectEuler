#!/bin/python3

__author__ = "Adam Karl"
"""If there are any Pythagorean triples for which a**2 + b**2 = c**2 and a + b + c = N, find the maximum value of abc. If there is no triple, print -1"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
#First line is T the number of cases, followed by T lines with values of N
#Constraints: 1 <= T <= 3000; 1 <= N <= 3000
#April 2018

import sys
from math import floor

def maxTriple(n):
    """Return the maximum product of abc for which a**2 + b**2 = c**2 and a + b + c = N"""
    if(n%2 != 0):
        return -1
    else:
        max_prod = -1
        for a in range(1, n//3 + 1):
            b = a ** 2 - (a - n) ** 2
            b /= 2
            b /= (a-n)
            if not b - floor(b) > 0:
                b = int(round(b))
                c = n-a-b
                if a**2 + b**2 == c**2:
                    if a*b*c > max_prod:
                        max_prod = int(a*b*c)
        return max_prod

def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = maxTriple(n)
        print(result)

if __name__ == "__main__":
    main()
