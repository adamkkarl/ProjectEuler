#!/bin/python3

__author__ = "Adam Karl"

"""Given an amount of money, find the number of unique ways to make that amount using English coins (up to 200p) mod 10**9 + 7"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler031
#First line t number of test cases, followed by t lines of N values (currency amounts)
#Constraints: 1 <= T <= 10 000; 1 <= N <= 100 000

memo = [] #memo[n] has the number of ways to make n pence using coins
coinValues = [1, 2, 5, 10, 20, 50, 100, 200]
MAXIMUM = 100001
MOD = 1000000007

def calculateCombinations(coinIndex, n):
    """Generate memoization where memo[7][n] contains the number of ways to make n pence of change"""
    global memo
    if coinIndex == 0: #always 1 way to make change if you only have 1p coins
        return 1
    if memo[coinIndex][n] != 0: #already in memo
        return memo[coinIndex][n]
    coinValue = coinValues[coinIndex]
    test_n = n
    combs = 0
    while test_n >= 0:
        combs += calculateCombinations(coinIndex - 1, test_n)
        if combs > MOD:
            combs %= MOD
        test_n -= coinValue
    memo[coinIndex][n] = combs #update memo
    return combs

def initializeMemo():
    """initialize memo with 0s, except first row which is all 1s"""
    global memo
    memo = [[0 for i in range(MAXIMUM)] for j in range(8)]
    memo[0] = [1 for i in range(MAXIMUM)]

def main():
    initializeMemo()
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = calculateCombinations(7, n)
        print(result)

if __name__ == "__main__":
    main()
