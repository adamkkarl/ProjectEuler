#!/bin/python3

__author__ = "Adam Karl"
"""What is the sum of digits of the number 2**N"""
#https://projecteuler.net/problem=16
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
    print("Find the sum of digits or 2 to what power? ", end="")
    n = int(input())
    result = power_digit_sum(n)
    print("Sum = %d" % result)

if __name__ == "__main__":
    main()
