#!/bin/python3

__author__ = "Adam Karl"
"""How many distinct terms are in the sequence a**b"""
#Constraints: 2 <= a <= 100; 2 <= b <= 100

fac = []

def generate_factorizations(N):
    """generate factorizations for numbers up to N"""
    fac = [[] for x in range(N+1)]

    fac[0] = 0
    fac[1] = 0 #0 and 1 don't have prime factorizations

    i = 2
    while i <= N:
        if fac[i] == []:
            cPrime = i
            ex = 1
            while pow(cPrime, ex) <= N:
                ex += 1
            ex -= 1
            while ex > 0:
                val = pow(cPrime, ex)
                mult = 1
                while val * mult <= N:
                    if mult % cPrime == 0:
                        mult += 1
                    else:
                        fac[val * mult].append([cPrime,ex])
                        mult += 1
                ex -= 1
        i += 1

#    print(fac)
#    for i in range(2, N+1):
#        print(i, ":", fac[i])
    print(fac[N])

def numDistinct(a, b):
    powList = []
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            powList.append(pow(i, j))
    powList.sort()
    numDistinct = 1
    index = 1
    while index < len(powList):
        if powList[index] != powList[index - 1]:
            numDistinct += 1
        index += 1
    return numDistinct

def main():
    N = int(input())
    print(numDistinct(N))

if __name__ == "__main__":
    main()
