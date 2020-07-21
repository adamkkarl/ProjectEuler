#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://www.hackerrank.com/contests/projecteuler/challenges/euler040/problem
#First line contains that denotes the number of test cases. This is followed by lines, each containing an integers. 
#Constraints: 1 <= T <= 100 000; 1 <= i <= 10**18

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
    t = int(input())
    for _ in range(t):
        indexes = list(map(int, input().split()))
        prod = 1
        for i in indexes:
            prod *= getNthDigit(i)
        print(prod)

if __name__ == "__main__":
    main()
