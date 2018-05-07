#!/bin/python3

__author__ = "Adam Karl"
"""Moving only right and down, how many paths are there to the end of a N by M grid?"""
#T number of test cases, followed by T lines of N M values
#Constraints: 1 <= T <= 1000; 1 <= N <= 500; 1 <= M <= 500
#April 2018

memo = [[0 for x in range(500)] for y in range(500)] #500x500 grid for storing 

def generateMemoization():
    """Fill the grid with number of routes for i by j grid when i <= j.
    It is only necessary to fill half since 5 by 6 has the same routes as 6 by 5"""
    memo[0][0] = 2 #for 1 by 1 grid
    for j in range(1, 500): #1 to 499 inclusive
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
    generateMemoization()
    t = int(input())
    p = int(1e9 + 7)
    for a0 in range(t):
        n,m = input().split()
        n,m = [int(n),int(m)]
        a = 0
        if n <= m:
            a = memo[n-1][m-1]
        else:
            a = memo[m-1][n-1]
        print(a % p)

if __name__ == "__main__":
    main()
