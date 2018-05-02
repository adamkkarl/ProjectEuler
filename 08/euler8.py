#!/bin/python3

__author__ = "Adam Karl"
"""Find the greatest product of K consecutive digits in the N digit number"""
#First line contains T the number of test cases
#each test case has N and K on the first line, and the N digit number on the second line
#Constraints: 1 <= T <= 100; 1 <= K <= 7; K <= N <= 1000

def main():
    t = int(input().strip())
    for _ in range(t):
        n,k = input().strip().split(' ')
        n,k = [int(n),int(k)]
        num = input().strip()
        
        max_prod = 0
        for start in range(n-k):
            product = 1
            for index in range(k):
                product *= int(num[start+index])
            if product > max_prod:
                max_prod = product
        print(str(max_prod))

if __name__ == "__main__":
    main()
