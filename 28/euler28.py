#!/bin/python3

__author__ = "Adam Karl"
"""Starting with 1 and moving out in a spiral, that is the sum of the diagonals in an N x N spiral"""
#https://projecteuler.net/problem=28

#NOTES
#top right of nxn is n**2
#bottom left of nxn is (n**2 + (n-2)**2)/2 This is also the average of top left, bot left, and bot right
#therefore, ans(n by n) = ans(n-2 by n-2) + 4n**2 - 6n + 6 (after expansion)

def sumOfDiagonal(n):
    """Sum the diagonals of a n x n spiral (1 in the middle then spiralling out)"""
    sum1 = (n * (n + 1) * (2 * n + 1)) // 3
    sum2 = ((n - 1) * (n - 1)) //2
    return sum1 - sum2 - 1
    
def main():
    print("Sum the diagonals of a n x n spiral. n = ", end="")
    n = int(input())
    result = sumOfDiagonal(n)
    print("Sum = %d" % result)

if __name__ == "__main__":
    main()
