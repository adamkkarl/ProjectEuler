#!/bin/python3

import sys, math

#Problem 42 Project Euler Solution
#https://projecteuler.net/problem=42

def isTriangleNum(n):
    """Given a word, return n if the sum of its letters is a triangle number, or -1 otherwise
    The equation for a triangle number is:
    t = (1/2)n(n+1)"""
    n *= 2
    v1 = math.floor(math.sqrt(n))
    v2 = v1 + 1
    if v1 * v2 == n:
        return v1
    return -1

def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(isTriangleNum(n))

if __name__ == "__main__":
    main()
