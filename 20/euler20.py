#!/bin/python

__author__ = "Adam Karl"
"""Find the sum of digits in the factorial of a number"""
#https://projecteuler.net/problem=20
#April 2018

from math import factorial

def sumOfDigits(n):
    """given int n, return sum of its digits"""
    s = str(n)
    my_sum = 0
    for digit in s:
        my_sum += int(digit)
    return my_sum
    
def main():
    print("Find the sum of the digits of x! where x = ", end="")
    n = int(input())
    fac = factorial(n)
    print("Sum of digits of %d! = %d" % (n, sumOfDigits(fac)))
        

if __name__ == "__main__":
    main()
