#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all numbers below N which divide the sum of the factorial of their digits"""
#https://projecteuler.net/problem=34

digitFactorials = []

def sumCuriousNumbersUnderN(n):
    """Return a sum of all numbers that evenly divide the sum of the factorial of their digits"""
    sumCurious = 0
    for i in range(10, n): #no numbers under 10 are curious, even though 1!=1 and 2!=2
        string = str(i)
        digitFactorialSum = 0
        for c in string:
            digitFactorialSum += digitFactorials[int(c)]
        if digitFactorialSum == i:
            sumCurious += i
    return sumCurious

def main():
    print("Find the sum of all numbers which are equal to the sum of the factorial of their digits")
    global digitFactorials
    digitFactorials = [1] #0! = 1
    for i in range(9): #1-9
        digitFactorials.append(digitFactorials[-1] * (i+1))
        
    #since 7 * 9! = 2540160, 2540160 is the last number that can be potentially curious
    result = sumCuriousNumbersUnderN(2540161)
    print("Sum = %d" % result)
    

if __name__ == "__main__":
    main()
