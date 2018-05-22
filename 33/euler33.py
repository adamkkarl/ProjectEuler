#!/bin/python3

__author__ = "Adam Karl"

def simplify(num, denom):
    """Given a numerator and denominator for a fraction, reduce it to lowest terms"""
    while num % 2 == 0 and denom % 2 == 0:
        num = num >> 1
        denom = denom >> 1
    
    factor = 3
    while factor <= num:
        while num % factor == 0 and denom % factor == 0:
            num = int(round(num / factor))
            denom = int(round(denom / factor))
        factor += 2
    return [num, denom]

def digitListToInt(arr):
    """Given list of string digits, convert to integer. If empty return 0"""
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return int(arr[0])
    else:
        return int("".join(arr))

def incorrectSimplify(num, denom):
    """Given a numerator and denominator, reduce it incorrectly by cancelling out digits (e.g. the 4s cancel in 34/49 to give 3/9"""
    numList = [x for x in str(num)]
    denomList = [x for x in str(denom)]
    for digit in numList:
        if digit in denomList and digit != '0':
            numList.remove(digit)
            denomList.remove(digit)
    return [digitListToInt(numList), digitListToInt(denomList)]

def main():
    numerators = []
    denominators = []
    for i in range(10, 100):
        for j in range(i + 1, 100):
            n1, n2 = simplify(i, j)
            i1, i2 = incorrectSimplify(i, j)
            i3, i4 = simplify(i1, i2)
            if n1 == i3 and n2 == i4 and i1 != i and i1 != j:
               numerators.append(i)
               denominators.append(j)
    print(numerators)
    print(denominators)
    totN = 1
    for n in numerators:
        totN *= n
    totD = 1
    for d in denominators:
        totD *= d
    print(simplify(totN, totD))

if __name__ == "__main__":
    main()
