#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all natural numbers less than N that are palindromes both in base 10 and base K"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler036
#First line has N K
#Constraints: 10 <= N <= 10**6; 2 <= K <= 9

def isPalindrome(s):
    """given a string s, recursively return True if it is a palindrome, False otherwise"""
    if s == s[::-1]:
        return True
    return False

def returnBaseK(n, k):
    """Given base 10 number n and base k, return n converted to base k as a string"""
    s = ""
    while n > 0:
        s = s + str(n % k)
        n  = int(round(n // k))
    return s[::-1]
    
def numPalindromes(n, k):
    """Given ints n and k, return the sum of the integers less than n that are palindromes both in base 10 and base k"""
    palindrome_sum = 0
    for i in range(n):
        if isPalindrome(str(i)) and isPalindrome(returnBaseK(i, k)):
            palindrome_sum += i
    return palindrome_sum

def main():
    n, k = list(map(int, input().split()))
    result = numPalindromes(n, k)
    print(result)

if __name__ == "__main__":
    main()
