#!/bin/python3

__author__ = "Adam Karl"
"""What us the smallest positive number that is evenly divisible by all numbers from 1 to N"""
#https://projecteuler.net/problem=5
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
    print("Find the smallest number divisible by all numbers 1 to: ", end="")
    n = int(input().strip())
    result = smallestMultiple(n)
    print(result)

if __name__ == "__main__":
    main()
