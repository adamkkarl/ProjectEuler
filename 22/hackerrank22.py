#!/bin/python3

__author__ = "Adam Karl"
"""Given a list of ~5000 names, find the score of a name based on the rules:
    letter score * ranking score where A=1, B=2, ... for letter score and the ranking is its place in the list once sorted alphabetically"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler022/problem
#First line N number of names, followed by N lines of names
#Followed by integer Q followed by Q lines each having a name
#Constraints: 1 <= N <= 5200, 1 <= Q <= 100

def charScore(c):
    """return character score for a character. 'A'=1,'B'=2, etc"""
    return ord(c) - ord('A') + 1

def main():
    names = list()
    numNames = int(input())
    for a0 in range(numNames):
        names.append(input())
    names.sort()
    
    t = int(input())
    for a0 in range(t):
        name = input()
        indexScore = names.index(name) + 1
        letterScore = 0
        for c in name:
            letterScore += charScore(c)
        totalScore = indexScore * letterScore
        print(totalScore)
    

if __name__ == "__main__":
    main()
