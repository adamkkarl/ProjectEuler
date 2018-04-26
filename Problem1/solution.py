#!/bin/python3

import sys

#Problem 1 Project Euler Solution
#Passes all test cases on HackerRank April 2018
    
def sum_multiples_of_three(n):
    """Returns the sum of all multiples of 3 from 0 to n (not including n)"""
    max_multiple = n - 1
    max_multiple = max_multiple - (max_multiple % 3) #finds the last multiple of 3 in the sum
    terms = round(max_multiple / 3)
    pair_val = (max_multiple + 3)
    return (terms * pair_val) >> 1
def sum_multiples_of_five(n):
    """Returns the sum of all multiples of 5 from 0 to n (not including n)"""
    max_multiple = n - 1
    max_multiple = max_multiple - (max_multiple % 5) #finds the last multiple of 5 in the sum
    terms = round(max_multiple / 5)
    pair_val = (max_multiple + 5)
    return (terms * pair_val) >> 1

def sum_multiples_of_fifteen(n):
    """Returns the sum of all multiples of 15 from 0 to n (not including n)"""
    max_multiple = n - 1
    max_multiple = max_multiple - (max_multiple % 15) #finds the last multiple of 15 in the sum
    terms = round(max_multiple / 15)
    pair_val = (max_multiple + 15)
    return (terms * pair_val) >> 1
    
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(str(sum_multiples_of_three(n) + sum_multiples_of_five(n) - sum_multiples_of_fifteen(n)))

