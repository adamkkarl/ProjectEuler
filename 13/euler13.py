#!/bin/python3

__author__ = "Adam Karl"
"""Work out the first ten digits of the sum of N 50-digit numbers"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem
#first line is N, the number of 50-digit numbers, the next N lines have a 50 ddigit number
#constraints: 1 <= N <= 1000
#April 2018
"""example input:
5
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676"""


def main():
    n = int(input())
    
    sum = 0
    for a0 in range(n):
        sum += int(input())
    print(str(sum)[:10])



if __name__ == "__main__":
    main()
