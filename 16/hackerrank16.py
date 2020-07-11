#!/bin/python3

__author__ = "Adam Karl"
"""What is the sum of digits of the number 2**N"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler016
#First line has T the number of test cases, followed by T lines of N values
#Constraints: 1 <= T <= 100; 1 <= N <= 10 000

def power_digit_sum(n):
    """Given integer n, return the sum of digits in 2**n"""
    i = 2 << (n-1)
    s = str(i)
    my_sum = 0
    for c in s:
        my_sum += int(c)
    return my_sum


def main():
    t = int(input())
    for a0 in range(t):
        n = int(input())
        result = power_digit_sum(n)
        print(result)

if __name__ == "__main__":
    main()
