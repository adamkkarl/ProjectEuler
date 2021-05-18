#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://www.hackerrank.com/contests/projecteuler/challenges/euler040/problem
#First line contains that denotes the number of test cases. This is followed by lines, each containing an integers.
#Constraints: 1 <= T <= 100 000; 1 <= i <= 10**18

numString = ""

def generateString():
    i = 0
    currNum = 1
    numString = ""
    while(len(numString) < pow(10, 5)):
        numString = numString + str(currNum)
        i += len(str(currNum))
        currNum += 1

def main():
    generateString()

    t = int(input())
    for _ in range(t):
        indexes = list(map(int, input().split()))
        prod = 1
        for i in indexes:
            prod *= int(numString[i])
        print(prod)

if __name__ == "__main__":
    main()
