#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://projecteuler.net/problem=40

def getNthDigit(n):
    """return the nth digit created by concatenating the positive integers"""
    """12345678910111213..."""
    i = 0
    currNum = 1
    while(True):
        i += len(str(currNum))
        if(i >= n):
            diff = i - n
            return int(str(currNum)[-1-diff])

        currNum += 1
    

def main():
    prod = 1
    prod *= getNthDigit(1)
    prod *= getNthDigit(10)
    prod *= getNthDigit(100)
    prod *= getNthDigit(1000)
    prod *= getNthDigit(10000)
    prod *= getNthDigit(100000)
    prod *= getNthDigit(1000000)
    print("d1 x d10 x d100 x ... x d1000000 = %d" % prod)

    

if __name__ == "__main__":
    main()
