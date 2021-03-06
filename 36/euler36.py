#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all natural numbers less than N that are palindromes both in base 10 and base K"""
#https://projecteuler.net/problem=36

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
    print("Find the sum of all integers that are palindromic in base 10, base 2, and are less than: ", end="")
    n = int(input())
    result = numPalindromes(n, 2)
    print("Sum = %d" % result)

if __name__ == "__main__":
    main()
