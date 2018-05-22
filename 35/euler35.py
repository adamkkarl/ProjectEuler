#!/bin/python3

__author__ = "Adam Karl"

isPrime = []

def generatePrimes(n):
    """given a maximum value n, fill an array of 1s and 0s for 0 to n-1 where isPrime[i] = 1 if i is a prime, or 0 if i is not"""
    global isPrime
    isPrime = [1 for i in range(n+1)]
    isPrime[0] = 0 #0 not prime
    isPrime[1] = 0 #1 not prime
    i = 0
    while i < n:
        if isPrime[i] == 1: #found a prime
            k = 2 * i
            while k < n: #all multiples of a prime are not prime
                isPrime[k] = 0
                k += i
        i += 1

def rotate(i, length):
    """Given integer i and number of digits, rotate its digits by 1 spot"""
    s = str(i)
    ans = 0
    if len(s) == 1:
        return i
    if len(s) == 2:
        ans = int(s[1] + s[0])
    else:
        ans = int(s[1:] + s[0])
    while len(str(ans)) < length: #solve for 011 being rotated to 11 instead of 110
        ans *= 10
    return ans

def circPrimesBelowN(n):
    """Given integer n, return the sum of all circular primes below n"""
    numCircs = 0
    for i in range(2, n):
        if isPrime[i] == 1:
            length = len(str(i))
            nextComb = rotate(i, length)
            isCirc = True
            while nextComb != i and isCirc:
                if not isPrime[nextComb] == 1:
                    isCirc = False
                nextComb = rotate(nextComb, length)
            if isCirc:
                numCircs += 1
    return numCircs


def main():
    n = int(input())
    generatePrimes(n)
    result = circPrimesBelowN(n)
    print(result)

if __name__ == "__main__":
    main()
