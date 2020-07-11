#!/bin/python3

__author__ = "Adam Karl"
"""Moving only right and down, how many paths are there to the end of a N by M grid?"""
#https://projecteuler.net/problem=15
#April 2018


def generateMemoization(n):
    """Fill the grid with number of routes for i by j grid when i <= j.
    It is only necessary to fill half since 5 by 6 has the same routes as 6 by 5"""
    global memo
    memo = [[0 for x in range(n)] for y in range(n)] #n x n grid for storing 
    memo[0][0] = 2 #for 1 by 1 grid
    for j in range(1, n): #1 to n-1 inclusive
        for i in range(j+1): #0 to j inclusive
           
            ans = 0
            if i == 0:
                ans = 1 + memo[i][j-1]
            else:
                ans += memo[i-1][j]
                if i < j:
                    ans += memo[i][j-1]
                else: #i == j and routes for a by b == routes for b by a
                    ans *= 2
            memo[i][j] = ans
                
def main():
    print("Number of rows and cols: ", end="")
    n = int(input())
    generateMemoization(n)
    a = memo[n-1][n-1]
    print("%d routes" % a)


if __name__ == "__main__":
    main()
