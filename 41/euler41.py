#!/bin/python3

import sys, math

__author__ = "Adam Karl"
#https://projecteuler.net/problem=41

def isPrime(n):
    """Return True if n is prime, False otherwise"""
    if (n % 2 == 0):
        return False
    divisor = 3
    root = math.ceil(math.sqrt(n))
    while (divisor <= root):
        if (n % divisor == 0):
            return False
        divisor += 2
    return True


def prevLexPermutation(s):
    """Given a string, return the previous lexicographic permutation"""
    """If the first permutation, return None"""
    l = [c for c in s]
    for i in range(len(l)-1, 0, -1):
        if(l[i-1] > l[i]):
            for j in range(len(l)-1, i-1, -1):
                if (l[j] < l[i-1]):
                    temp = l[j]
                    l[j] = l[i-1]
                    l[i-1] = temp
                    
                    end = l[i:]
                    end.reverse()
                    return "".join(l[:i] + end)
    return None

def largestNdigitPandigitalPrime(n):
    """Return the largest pandigital prime with n digits"""
    """Returns None if there aren't any"""
    s = "987654321"[9-n:]
    #at this point, s is the string of the last pandigital (e.g. "54321")
    while(s != None):
        if(isPrime(int(s))):
            return int(s)
        s = prevLexPermutation(s)
    return None

def main():    
    p = None
    for i in range(9, 0, -1):
        p = largestNdigitPandigitalPrime(i)
        if(p != None):
            break
    print("The largest pandigital prime is %d" % p)

if __name__ == "__main__":
    main()
