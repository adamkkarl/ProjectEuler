#!/bin/python3

__author__ = "Adam Karl"
#https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
#For T values of N, find the sum of all even Fibonacci numbers less than or equal to N
#Constraints: 1 <= T <= 10**5; 10 <= N <= 4 * 10**16
#April 2018

import sys

def fib(n1, n2, maximum):
    new = n1 + n2
    if new > maximum:
        return 0
    
    if new % 2 == 0:
        return new + fib(n2, new, maximum)
    return fib(n2, new, maximum)
    
def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(str(fib(1, 1, n)))


if __name__ == "__main__":
    main()
