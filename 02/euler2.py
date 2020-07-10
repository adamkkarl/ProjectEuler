#!/bin/python3

__author__ = "Adam Karl"
#https://projecteuler.net/problem=2
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
    print("Sum even Fibonacci numbers below: ", end="")
    n = int(input().strip())
    print("Sum = %d" % (fib(1, 1, n)))


if __name__ == "__main__":
    main()
