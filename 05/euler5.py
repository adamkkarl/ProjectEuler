#!/bin/python3

__author__ = "Adam Karl"
"""What us the smallest positive number that is evenly divisible by all numbers from 1 to N"""
#First line has T the number of test cases, followed by T lines each with N values
#Constraints: 1 <= T <= 10; 1 <= N <= 40
#April 2018

import sys

def smallestMultiple(n):
        product = 1
        products = []
        for factor in range(2,n + 1):
            for j in products:
                if factor % j == 0:
                    factor /= j
            product *= factor
            products.append(factor)
        return int(round(product))

def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = smallestMultiple(n)
        print(result)

if __name__ == "__main__":
    main()
