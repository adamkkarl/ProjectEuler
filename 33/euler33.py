#!/bin/python3

__author__ = "Adam Karl"
"""49/98 is curious since a naiive mathematician might simplify by just cancelling the '9's in the fraction leaving 4/8 (which is actually a valid simplification). Given N, the number of digits in the numerator and denominator, and K the number of integers to cancel, find every non-trivial solution and return the sum of the numerators and sum of the denominators"""
#https://www.hackerrank.com/contests/projecteuler/challenges/euler033
#Input: N K
#Constraints: 2 <= N <= 4; 1 <= K <= N-1

#TODO: allow for all permutations of removals: 4808/8414 => 8/14 for n=4, k=2

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
    """Given a numerator and denominator, reduce it incorrectly by cancelling out digits. Also return the number of pairs of digits canceled out (e.g. the 4s cancel in 34/49 to give 3/9, and returns 1 pair canceled)"""
    numList = [x for x in str(num)]
    denomList = [x for x in str(denom)]
    digitsCanceled = 0
    for digit in numList:
        if digit in denomList and digit != '0':
            numList.remove(digit)
            denomList.remove(digit)
            digitsCanceled += 1
    return [digitListToInt(numList), digitListToInt(denomList), digitsCanceled]

def main():
    numeratorProd = 1
    denominatorProd = 1

    print("Calculating curious fractions with 2-digit numerators and demoninators", flush=True)

    n=2 #2 digits
    k=1 #cancel exactly 1 digit from num & denom
    min_numerator = pow(10, n - 1)
    max_numerator = pow(10, n)
    for numerator in range(min_numerator, max_numerator): #10 to 98
        denominator = numerator+1
        while(denominator < max_numerator): #numerator+1 to 99
            inc_num, inc_denom, test_k = incorrectSimplify(numerator, denominator)
            if test_k == k:
                inc_num, inc_denom = simplify(inc_num, inc_denom)
                cor_num, cor_denom = simplify(numerator, denominator)
                if inc_num == cor_num and inc_denom == cor_denom:
                    print("%d/%d" % (numerator, denominator), end=" ", flush=True)
                    numeratorProd *= numerator
                    denominatorProd *= denominator
            denominator += 1
    print()
    num, denom = simplify(numeratorProd, denominatorProd)
    print("Product of curious fractions = %d/%d" % (num, denom))

if __name__ == "__main__":
    main()
