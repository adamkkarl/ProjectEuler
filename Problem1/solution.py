#!/bin/python3

import sys

#Problem 1 Project Euler Solution
#Passes all test cases on HackerRank April 2018
#Constraints: 1 <= T <= 10**5; 1 <= N <= 10**9
#https://www.hackerrank.com/contests/projecteuler/challenges/euler001

def sum_multiples_of_k(n, k):
    """Finds the sum of all multiples of k that are less than n"""
    max_multiple = n - 1
    max_multiple = max_multiple - (max_multiple % k) #finds last multiple of 3 in the sum
    terms = int(round(max_multiple / k))
    pair_val = (max_multiple + k)
    return (terms * pair_val) >> 1
    
def main():    
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        
        print(str(sum_multiples_of_k(n, 3) + sum_multiples_of_k(n, 5) - sum_multiples_of_k(n, 15)))

if __name__ == "__main__":
    main()
