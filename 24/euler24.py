#!/bin/python3

__author__ = "Adam Karl"
"""What is the Nth lexiographic permutation of 0123456789"""
#https://projecteuler.net/problem=24

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
    chars = ['0','1','2','3','4','5','6','7','8','9']

    print("Find the nth permutation of 0123456789. n = ", end="")
    n = int(input())

    generateFactorials()
    printChars(chars, n)
    print()
    

if __name__ == "__main__":
    main()
