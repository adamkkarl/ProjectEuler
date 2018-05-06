#!/bin/python3

__author__ = "Adam Karl"
"""Triangle numbers are formed by adding all natural numbers up to a maximum. i.e. the Nth
natural number is 1+2+...+N. What is the first triangle number to have over N divisors"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem
#first line t is the numebr of test cases, followed by t lines of N values
#Constraints: 1 <= T <= 10; 1 <= N <= 1000
#April 2018


from math import sqrt, ceil

def findDivisors(n):
    """find and return the number of divisors in n (the last number appended to triangles)"""
    primeFactors = dict()
    while n % 2 == 0: #test separately since only even prime
        if 2 in primeFactors.keys():
            primeFactors[2] += 1
        else:
            primeFactors[2] = 1
        n /= 2
    
    testFactor = 3 #only test odd factors from here on out
    sq_root = int(ceil(sqrt(n))) + 1
    while testFactor < sq_root:
        if n % testFactor == 0: #found a factor
            if testFactor in primeFactors.keys():
                primeFactors[testFactor] += 1
            else:
                primeFactors[testFactor] = 1
            n /= testFactor
            sq_root = int(ceil(sqrt(n)))
        else:
            testFactor += 2
    n = int(round(n))
    if n > 1:
        if n in primeFactors.keys():
            primeFactors[n] += 1
        else:
            primeFactors[n] = 1
            
    numDivisors = 1
    for i in primeFactors.keys():
#        print(str(i) + "^" + str(primeFactors[i]))
        numDivisors *= (primeFactors[i]+1)
        
    return numDivisors

def main():
    triangles = [0,1,3]
    divisors = [0,1,2]
    length = 3
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        found = False
        index = 1
        while index < length and not found: #first check if it's already in our list of triangles
            if divisors[index] > n: #found our answer
                print(triangles[index])
                found = True
            index += 1
        
        while not found: #need to add to triangles/divisors
            triangles.append(triangles[-1] + length)
            divisors.append(findDivisors(triangles[-1]))
            length += 1
            if divisors[-1] > n:
                print(triangles[-1])
                found = True

if __name__ == "__main__":
    main()
