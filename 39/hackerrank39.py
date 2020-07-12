#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem
#First line contains T that denotes the number of test cases. this is followed by T lines, each containing and integer, N
# 1 <= T <= 100 000
# 12 <= N <= 5 000 000

isSquare = [False for i in range(2500000)] #max perim=5m so max side < 2.5m
numTriangles = [0 for i in range(5000001)] #numTriangles[p] has # right triangles with perimeter of p
maxP = [0 for i in range(5000001)] #maxP[i] has the value of p that maximizes # of right triangles

def generateIsSquare():
    """isSquare[i] is True iff i is a square number"""
    i = 1
    sq = 1
    while(sq <= 2500000):
        isSquare[sq] = True
        i += 1
        sq = pow(i,2)


def isSquareNum(n):
    """Return if n is square or not"""
    if(n<2500000):
        return isSquare[n]
    i = 1582
    while(True):
        if(pow(i,2 < n)):
            i += 1
        elif(pow(i,2) > n):
            return False
        elif(pow(i,2) == n):
            return True

def generateNumTriangles():
    """numTriangles[i] contains the number of right triangles with perimeter=i"""
    a = 1
    while(a<2500000):
        b = a
        while(a+b < 25000000):
            if(isSquareNum(a**2+b**2)): #if c is square number
                c = sqrt(a**2+b**2)
                numTriangles[a+b+c] += 1
            b += 1
        a += 1

def calcMaxP():
    """maxP[i] has the value of p <= i that generates the most right triangles"""
    mTris = 0
    mP = 0
    for p in range(5000001):
        if(maxTris < numTriangles[p]): #found new max
            maxP[p] = p
            mP = p
            mTris = numTriangles[p]
        else:
            maxP[p] = mP

def main():    
    generateIsSquare()
    generateNumTriangles()
    print("2", flush=True)
    calcMaxP()
    print("ready", flush=True)
    t = int(input())
    for _ in range(t):
        p = int(input())
        print(maxP[p])

if __name__ == "__main__":
    main()
