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

def inAbundantsList(n):
    """Return True if item is in list of abundants, False otherwise"""
    for a in abundants:
        if a == n:
            return True
        if a > n:
            return False
    return False
        
def canBeWritten(n):
    """Return True if N can be written as the sum of 2 abundant numbers, False if it cannot"""
    if n > 28123:
        return True
    if n < 24:
        return False
    for a in abundants:
        if a > n:
            return False
        if inAbundantsList(n - a):
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
#    main()
    generateAbundants()
    my_sum = 0
    for i in range(28124):
        if not canBeWritten(i):
            print(i)
            my_sum += i
    print(my_sum)
