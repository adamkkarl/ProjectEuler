#!/bin/python3

import sys

__author__ = "Adam Karl"
#https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem
#First line contains T that denotes the number of test cases. this is followed by T lines, each containing and integer, N
# 1 <= T <= 100 000
# 12 <= N <= 5 000 000

#NOTES: the perimeter of a right triangle is always even

roots = dict()
numTriangles = [0 for i in range(5000001)] #numTriangles[p] has # right triangles with perimeter of p
maxP = [0 for i in range(5000001)] #maxP[i] has the value of p that maximizes # of right triangles

#TODO euclid's method to generate pythagorean triples

def generateRoots():
    """fill roots with [a**2,a] pairs"""
    i = 1
    sq = 1
    while(i <= 2500000):
        roots[pow(i,2)] = i
        i += 1

def isSquareNum(n):
    """Return if n is square or not"""
    if(roots.get(n) != None):
        return True
    return False


def generateNumTriangles():
    """numTriangles[i] contains the number of right triangles with perimeter=i"""
    c = 2500000 #max perimeter=5m, so max hypot=2.5m
    c2 = pow(c,2)
    while(c>0):
        print(c, flush=True)
        a = 1
        while(a < c):
            a2 = pow(a,2)
            if(isSquareNum(c2-a2)): #if b is square
                b = roots[c2-a2]
                if(a <= b and b < c and a+b<c):
                    numTriangles[a+b+c] += 1
            a += 1
        c -= 1
        c2 = pow(c,2)

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
    generateRoots()
    print(1, flush=True)
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
