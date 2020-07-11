#!/bin/python3

__author__ = "Adam Karl"
"""Given a list of ~5000 names, find the score of a name based on the rules:
    letter score * ranking score where A=1, B=2, ... for letter score and the ranking is its place in the list once sorted alphabetically"""
#https://projecteuler.net/problem=22

def charScore(c):
    """return character score for a character. 'A'=1,'B'=2, etc"""
    return ord(c) - ord('A') + 1

def main():
    print("scoring all names in names.txt")
    
    f = open("names.txt", "r")
    text = f.read()
    f.close()

    names = text.split(",")
    names.sort()

    totalScore = 0
    for i in range(0, len(names)):
        indexScore = i + 1
        lettersScore = 0
        for c in names[i]:
            if c != "\"":
                lettersScore += charScore(c)
        wordScore = indexScore * lettersScore
        totalScore += wordScore
    
    print("Sum of scores = %d" % totalScore)
    

if __name__ == "__main__":
    main()
