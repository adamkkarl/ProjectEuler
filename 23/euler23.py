#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all positive integers which cannot be written as the sum of two abundant numbers"""
#https://projecteuler.net/problem=23

from math import sqrt, ceil

abundants = [] #used to store an ascending list of all abundant numbers < 28124
canBeWritten = [] #[i] is true if i can be summed by 2 abundants, false otherwise

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
        return True
    return False

def generateAbundants():
    """Generate list of abundant numbers < 28124"""
    for testAbundant in range(1, 28124):
        if isAbundant(testAbundant):
            abundants.append(testAbundant)
    abundants.sort()

def generateCanBeWritten():
    """Generate list where canBeWritten[i] == true iff i can be written as a sum of 2 abundant numbers"""
    global canBeWritten
    canBeWritten = [False for i in range(28124)] #0 to 28123, inclusive
    numAbundants = len(abundants)
    for i in range(0, numAbundants-1):
        for j in range(i+1, numAbundants):
            val = abundants[i] + abundants[j]
            if(val <= 28123):
                canBeWritten[val] = True

def main():
    print("Summing all positive integers that cannot be written as the sum of two abundant numbers", flush=True)

    generateAbundants()

    generateCanBeWritten()
    
    sum = 0
    for i in range(1, 28124): #all numbers >28123 can be written as sum of 2 abundants
        if not canBeWritten[i]:
            sum += i
    print("Sum = %d" % sum)


if __name__ == "__main__":
    main()
