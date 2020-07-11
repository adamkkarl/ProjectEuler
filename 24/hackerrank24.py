#!/bin/python3

__author__ = "Adam Karl"
"""What is the Nth lexiographic permutation of abcdefghijklm"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler024/problem
#first line T number of test cases, followed by T lines of N values
#constraints: 1 <= T <= 1000; 1 <= N <= 13!

factorials = []

def generateFactorials():
    for i in range(12): #0-12 for factorials 1! to 12!
        factorials.append(factorial(i+1))
        
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def printChars(letters, n):
    if n == 1:#print out the rest normally
        for c in letters:
            print(c,end="")
    elif len(letters) == 2:
        if n == 2:
            print(str(letters[1]) + str(letters[0]),end="")
        else:
            print("ERROR" + str(n))
    else:
    
        length = len(letters) - 1 
        combinationsForRestOfDigits = factorials[length-1]
        index = 0

        while n > combinationsForRestOfDigits:
            index += 1
            n -= combinationsForRestOfDigits
        print(letters.pop(index),end="") #remove from list and print 
        printChars(letters, n)


def main():
    generateFactorials()
    t = int(input())
    for _d in range(t):
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
        n = int(input()) 
        printChars(letters, n)
        print()
    

if __name__ == "__main__":
    main()
