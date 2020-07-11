#!/bin/python3

__author__ = "Adam Karl"
"""Starting with 1 and moving out in a spiral, that is the sum of the diagonals in an N x N spiral"""
#first line T number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 10**5; 1 <= N < 10**18; N is odd

#NOTES
#top right of nxn is n**2
#bottom left of nxn is (n**2 + (n-2)**2)/2 This is also the average of top left, bot left, and bot right
#therefore, ans(n by n) = ans(n-2 by n-2) + 4n**2 - 6n + 6 (after expansion)

MOD = pow(10, 9) + 7
#def sumOfDiagonal(n):
#    """for and n x n square (n is odd), return sum of \ diagonal"""
#    """each value in the diagonal increases by 2, 4, 6, .. starting at 1 up to a maximum less than n**2"""
#    if n == 1:
#        return 1
#    outerShellSum = 4 * pow(n, 2) - 6 * n + 6
#    return (outerShellSum % MOD) + sumOfDiagonal(n - 2)

def sumOfDiagonal(n):
    sum1 = (n * (n + 1) * (2 * n + 1)) // 3
    sum2 = ((n - 1) * (n - 1)) //2
    return sum1 - sum2 - 1
    
def main():
    t = int(input())
    for a0 in range(t):
        n = int(input())
        result = sumOfDiagonal(n)
        print(result % MOD)

if __name__ == "__main__":
    main()
