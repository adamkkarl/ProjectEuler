#!/bin/python

__author__ = "Adam Karl"
"""Find the sum of digits in the factorial of a number"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem
#First line T number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 100; 0 <= N <= 1000
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
    t = int(input())
    for a0 in range(t):
        n = int(input())
        fac = factorial(n)
        print(sumOfDigits(fac))
        

if __name__ == "__main__":
    main()
