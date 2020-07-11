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

def generateMemo():
    """fill memo by passing over it once for each progressively larger coin value to find combinations
    for N using up to each maximum coin"""
    global memo
    memo = [1 for i in range(MAXIMUM)] #all ones for coinValue = 1
    for coinIndex in range(1, 8):
        coinValue = coinValues[coinIndex]
        for n in range(coinValue, MAXIMUM):
            memo[n] = (memo[n] + memo[n - coinValue]) % MOD

def main():
    generateMemo()
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = memo[n]
        print(result)

if __name__ == "__main__":
    main()
