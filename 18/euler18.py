#!/bin/python3

__author__ = "Adam Karl"
"""Find the maximum sum from following a path down a triangle of numbers"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler018/problem
#First line T number of test cases
#For each test case first line N number of rows in triangle, followed by N lines
#for which the ith line has i numbers
#Constraints: 1 <= T <= 10; 1 <= N <= 15; 0 <= numbers < 100
"""Sample input:
1
4
3
7 4
2 4 6
8 5 9 3
"""

def maximize(pyramid):
    """Recursively find the maximum path for the pyramid"""
    row = len(pyramid) - 2 #last row remains unchanged
    while row >= 0:
        numItems = row + 1
        for i in range(numItems):
            maxNext = pyramid[row+1][i]
            if maxNext < pyramid[row+1][i+1]:
                maxNext = pyramid[row+1][i+1]
            pyramid[row][i] = pyramid[row][i] + maxNext
        row -= 1
    return pyramid

def main():
    t = int(input())
    for a0 in range(t):
        numRows = int(input())
        pyramid = []
        for a0 in range(numRows):
            pyramid.append(list(map(int,input().split())))
        pyramid = maximize(pyramid)
        print(pyramid[0][0])


if __name__ == "__main__":
    main()
