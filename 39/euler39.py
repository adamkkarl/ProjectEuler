#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://projecteuler.net/problem=39

def testRightTriangle(a, b, c):
    """Return true if the 3 side lengths make a right triangle"""
    if (a+b > c and a**2+b**2==c**2):
        return True
    return False

def numRightTriangles(p):
    """Given the perimeter, find the number of integer right triangles"""
    numTriangles = 0
    a = 1
    while(a < p):
        b = a
        while(0 < p-a-b): #c>0
            if(testRightTriangle(a, b, p-a-b)):
                numTriangles += 1
            b += 1
        a += 1
    return numTriangles

def main():    
    print("Maximize the integer right triangle solutions for a+b+c=p where p <= ", end="")
    p = int(input())
    
    maxP = 0
    maxNum = 0
    for i in range(p+1):
        testNum = numRightTriangles(i)
        if(testNum > maxNum):
            maxP = i
            maxNum = testNum
    print("p = %d makes %d right triangles" % (maxP, maxNum))

if __name__ == "__main__":
    main()
