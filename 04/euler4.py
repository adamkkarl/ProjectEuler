#!/bin/python3

"""Find the largest palindrome made from the product of two 3-digit numbers less than N"""
__author__ = "Adam Karl"
#https://projecteuler.net/problem=4
#April 2018

import sys

def isPalindrome(n):
    """returns if a number is palindromic"""
    s = str(n)
    if s == s[::-1]:
        return True
    return False

def main():
    print("Find the largest palindrom made from two 3-digit numbers less than: ", end="")
    n = int(input().strip())
    
    largest_pal_product = 0
    for larger in range(318, 1000): #318 * 318 is the first square > 101101
        smaller = largest_pal_product // larger #dont care if we find palindromes < the max we've already found
        while larger * smaller < n and smaller <= larger:
            if (larger * smaller) > largest_pal_product:
                if isPalindrome(larger * smaller):
                    largest_pal_product = larger * smaller
            smaller += 1
    print(str(largest_pal_product))

if __name__ == "__main__":
    main()
