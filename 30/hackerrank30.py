#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all numbers that can be written as the Nth power of their digits"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler030/problem
#first line N
#Constraints: 3 <= N <= 6

powers = [0] * 10

def sumOfDigitsToN(i, n):
    """return the sum of the digits in i to the nth power"""
    sum = 0
    s = str(i)
    for digit in s:
        sum += powers[int(digit)]
    return sum

def sumOfNthDigitPowers(n):
    """Find the sum of all the numbers that can be written as the Nth sum of powers of their digits"""
    result = 0
    
    maxTestableNumber = 0 
    
    maxNumDigits = 2
    #while maximum we can make with this number of digits >= smallest number with that many digits
    while len(str(maxNumDigits * pow(9, n))) >= maxNumDigits:
        maxNumDigits += 1
    maxNumDigits -= 1 #since we've gone 1 digit too far
    
    maxTestableNumber = maxNumDigits * pow(9, n) + 1 #+1 since we use range() function
    for i in range(10, maxTestableNumber):
        if i == sumOfDigitsToN(i, n): #if True, found a number that can be written as its digits to n
            result += i
    return result

def main():
    n = int(input())
    
    global powers
    for i in range(10):
        powers[i] = pow(i,n)
    
    result = sumOfNthDigitPowers(n)
    print(result)

if __name__ == "__main__":
    main()
