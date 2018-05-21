#!/bin/python3

__author__ = "Adam Karl"
"""Find the sum of all products whose multiplicand/multiplier/product can be written as 1 through N  pandigital"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler032/problem
#Input: N
#Constraints: 4 <= N <= 9

from itertools import permutations

def sumOfPandigitals(n):
    """Given the number of digits (n), find the sum of all products that can be written
    as an equation using the digits 1 to n ex: 39 * 186 = 7254 uses 1 to 9"""
    nums = list(map(str,list(range(1, n+1))))
    perms = list(permutations(nums))
    products = []
    
    for p in perms:
        for x in range(1, n//2 + 1): #x divides a and b in a * b = c
            for y in range(x+1, n//2 + 2):#y divides b and c in a * b = c
                a = int(''.join(p[:x]))
                b = int(''.join(p[x:y]))
                c = int(''.join(p[y:]))
                if a * b == c:
                    if not c in products:
                        products.append(c)
    return sum(products)
            
def main():
    n = int(input().strip())
    result = sumOfPandigitals(n)
    print(result)

if __name__ == "__main__":
    main()
