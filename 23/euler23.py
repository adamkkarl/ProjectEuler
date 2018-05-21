#!/bin/python3

__author__ = "Adam Karl"
"""Given a number N, print "YES" if it can be expressed as a sum of two abundant numbers, otherwise print 'NO' """
#https://www.hackerrank.com/contests/projecteuler/challenges/euler023
#First line T has number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 100; 0 <= N <= 10 000

from math import sqrt, ceil

abundants = []
sums = []

def isAbundant(n):
    """Return True if n is an abundant number, False if it is not"""
    sumOfDivs = 1
    sq_root = int(ceil(int(sqrt(n))))
    for testFactor in range(2, sq_root + 1):
        if n % testFactor == 0:
            sumOfDivs += testFactor
            pair = int(n / testFactor)
            if pair != testFactor:
                sumOfDivs += pair
    if sumOfDivs > n:
        sums.append(sumOfDivs)
        return True
    return False

def generateAbundants():
    """Generate list of abundant numbers < 28123"""
    for testAbundant in range(1, 28123):
        if isAbundant(testAbundant):
            abundants.append(testAbundant)
    abundants.sort()
        
def canBeWritten(n):
    """Return True if N can be written as the sum of 2 abundant numbers, False if it cannot"""
    if n > 28123:
        return True
    if n < 24:
        return False
    max_index = 0
    length = len(abundants)
    while max_index + 1 < length and abundants[max_index] < n:
        max_index += 1
    
    for a in range(max_index):
        for b in range(a, max_index):
            if abundants[a] + abundants[b] == n:
                return True
    return False


def main():
    generateAbundants()

    t = int(input())
    for a0 in range(t):
        n = int(input())
        if canBeWritten(n):
            print("YES")
        else:
            print("NO")
        

if __name__ == "__main__":
    main()
