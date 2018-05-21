#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all numbers below N which divide the sum of the factorial of their digits"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler034/copy-from/1307250873
#Input: N
#Constraints: 10 <= N <= 10**5

digitFactorials = []

def curiousNumbersUnderN(n):
    """Return a sum of all numbers that evenly divide the sum of the factorial of their digits"""
    sumCurious = 0
    for i in range(10, n):
        string = str(i)
        digitFactorialSum = 0
        for c in string:
            digitFactorialSum += digitFactorials[int(c)]
        if digitFactorialSum % i == 0:
            sumCurious += i
    return sumCurious

def main():
    global digitFactorials
    digitFactorials = [1] #0! = 1
    for i in range(9): #1-9
        digitFactorials.append(digitFactorials[-1] * (i+1))
        
    n = int(input().strip())
    result = curiousNumbersUnderN(n)
    print(result)
    

if __name__ == "__main__":
    main()
