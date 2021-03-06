#!/bin/python3

__author__ = "Adam Karl"

"""Given an amount of money, find the number of unique ways to make that amount using English coins (up to 200p) mod 10**9 + 7"""
#https://projecteuler.net/problem=31

memo = [] #memo[n] has the number of ways to make n pence using coins
coinValues = [1, 2, 5, 10, 20, 50, 100, 200]
max = 100001

def generateMemo():
    """fill memo by passing over it once for each progressively larger coin value to find combinations
    for N using up to each maximum coin"""
    global memo
    memo = [1 for i in range(max+1)] #all ones for coinValue = 1
    for coinIndex in range(1, 8):
        coinValue = coinValues[coinIndex]
        for n in range(coinValue, max+1):
            memo[n] = (memo[n] + memo[n - coinValue])

def main():
    global max
    print("How many ways can you make __p out of 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p)? ")
    max = int(input())
    generateMemo()
    result = memo[max]
    print("%d ways" % result)

if __name__ == "__main__":
    main()
