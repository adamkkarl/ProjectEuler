#!/bin/python3

__author__ = "Adam Karl"
"""Evaluate the sum of all amicable numbers under N"""
#https://projecteuler.net/problem=21

from math import sqrt, ceil

listOfAmicables = []
sumOfDivisorsMemo = []

def generateAmicables(n):
    """Generate a list of amicable numbers <= 100 000"""   
    for a in range(2, n+1):
        b = sumOfDivisors(a, n)
        if a != b and a == sumOfDivisors(b, n):
            listOfAmicables.append(a)

def sumOfDivisors(a, n):
    """Return the sum of all divisors of a, including 1 and a"""
    if a > 0 and a <= n and sumOfDivisorsMemo[a-1] != -1:
        return sumOfDivisorsMemo[a-1]
    
    my_sum = 1
    testFac = 2
    sq_root = ceil(sqrt(a))
    while testFac <= sqrt(a):
        if a % testFac == 0:
            pair = int(a / testFac)
            if pair != testFac:
                my_sum += testFac + pair
            else:
                my_sum += testFac
        testFac += 1
    if a <= n:
        sumOfDivisorsMemo[a-1] = my_sum
    return my_sum

def main():
    print("Sum all amicable numbers under: ", end="")
    n = int(input())
    global sumOfDivisorsMemo
    sumOfDivisorsMemo = [-1] * n #sumof

    sumOfDivisorsMemo[0] = 0 #n = 1 has sum of divisors of 0
    sumOfDivisorsMemo[1] = 1 #n = 2 has sum of divisors of 1
    generateAmicables(n)
    numAmicables = len(listOfAmicables)
    
    sum_of_amicables = 0
    index = 0
    while index < numAmicables and listOfAmicables[index] < n:
        sum_of_amicables += listOfAmicables[index]
        index += 1
    print("Sum = %d" % sum_of_amicables)
                
    
if __name__ == "__main__":
    main()
