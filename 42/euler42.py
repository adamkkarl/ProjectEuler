#!/bin/python3

import sys

#Problem 42 Project Euler Solution
#https://projecteuler.net/problem=42

def isTriangleNum(n):
    """Given a number, return True if it is a triangle number"""
    n *= 2
    v1 = 1
    v2 = 2
    while True:
        if n == v1 * v2:
            return True
        elif n < v1 * v2:
            return False
        else:
            v1 += 1
            v2 += 1

def isTriangleWord(w):
    """Given a word, return True if the sum of its letters is a triangle number"""
    sum = 0
    for c in w:
        sum += ord(c) - ord('A') + 1    # +1 since 'A' has value 1
    if isTriangleNum(sum):
        return True

def main():
    filename = "words.txt"
    with open(filename) as f:
        content = f.readlines()

    num_words = 0
    num_twords = 0
    for line in content:
        words = line.split(',')
        for w in words:
            if(isTriangleWord(w[1:-1])):
                num_twords += 1
            num_words += 1

    print(num_twords, "of", num_words, "words are triangle words")

if __name__ == "__main__":
    main()
