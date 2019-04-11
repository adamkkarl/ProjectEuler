#!/bin/python3

__author__ = "Adam Karl"

#Input: N K

def largestPandigitalToK(n, k):
    largest = -1
    for mult in range(1, n):
        

def main():
    n, k = list(map(int, input().split()))
    result = largestPandigitalToK(n, k)
    print(result)
        

if __name__ == "__main__":
    main()
