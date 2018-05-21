#!/bin/python3

__author__ = "Adam Karl"
"""How many distinct terms are in the sequence a**b"""
#Constraints: 2 <= a <= 100; 2 <= b <= 100

def numDistinct(a, b):
    powList = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            powList.append(pow(i, j))
    powList.sort()
    print(powList)
    numDistinct = 1
    index = 1
    while index < len(powList):
        if powList[index] != powList[index - 1]:
            numDistinct += 1
        index += 1
    return numDistinct

def main():
    a = int(input())
    b = a
    result = numDistinct(a, b)
    print(result)

if __name__ == "__main__":
    main()
