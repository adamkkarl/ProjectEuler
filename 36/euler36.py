#!/bin/python3

__author__ = "Adam Karl"

def isPalindrome(s):
    """given a string s, recursively return True if it is a palindrome, False otherwise"""
    if s == s[::-1]:
        return True
    return False

def numPalindromes(n):
    """Given int n, return the sum of the integers less than n that are palindromes both in base 10 and binary"""
    palindrome_sum = 0
    for i in range(n):
        if isPalindrome(str(i)) and isPalindrome("{0:b}".format(i)):
            palindrome_sum += i
    return palindrome_sum


def main():
    n = int(input())
    result = numPalindromes(n)
    print(result)

if __name__ == "__main__":
    main()
