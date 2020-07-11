#!/bin/python3

__author__ = "Adam Karl"
"""Evaluate the sum of all amicable numbers under N"""
#https://projecteuler.net/problem=21

from math import sqrt, ceil

listOfAmicables = []
sumOfDivisorsMemo = [-1] * 100000 #sumOfDivisors[n-1] has the sum of divisors for n 


def generateAmicables():
    """Generate a list of amicable numbers <= 100 000"""   
    for a in range(2, 100001):
        b = sumOfDivisors(a)
        if a != b and a == sumOfDivisors(b):
            listOfAmicables.append(a)

def sumOfDivisors(n):
    """Return the sum of all divisors of N, including 1 and N"""
    if n > 0 and n <= 100000 and sumOfDivisorsMemo[n-1] != -1:
        return sumOfDivisorsMemo[n-1]
    
    
    my_sum = 1
    testFac = 2
    sq_root = ceil(sqrt(n))
    while testFac <= sqrt(n):
        if n % testFac == 0:
            pair = int(n / testFac)
            if pair != testFac:
                my_sum += testFac + pair
            else:
                my_sum += testFac
        testFac += 1
    if n <= 100000:
        sumOfDivisorsMemo[n-1] = my_sum
    return my_sum

def main():
    print("Sum all amicable numbers under: ", end="")
    n = int(input())

    sumOfDivisorsMemo[0] = 0 #n = 1 has sum of divisors of 0
    sumOfDivisorsMemo[1] = 1 #n = 2 has sum of divisors of 1
    generateAmicables()
    numAmicables = len(listOfAmicables)
    
    sum_of_amicables = 0
    index = 0
    while index < numAmicables and listOfAmicables[index] < n:
        sum_of_amicables += listOfAmicables[index]
        index += 1
    print("Sum = %d" % sum_of_amicables)
                
    
if __name__ == "__main__":
    main()
