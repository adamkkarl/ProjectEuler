#!/bin/python3

"""What is the first Fibonacci number to contain N digits"""
#https://projecteuler.net/problem=25

#fibNums = [1,1]
fibIndex = [1] #fibIndex[n-1] has the index of the first fibonacci number with at least n digits

def generateFibonacciIndexes():
    """if the last number in fibNums isnt long enough, keep appending new ones until it is"""
    """Return True if we had to add numbers (so our answer is the last one)"""
    appended = False
    a = 1
    b = 1
    index = 3
    length = 1
    while length < 5001:
        c = a + b
        if len(str(c)) > length:
            fibIndex.append(index)
            length += 1
        a = b
        b = c
        index += 1

def main():
    print("Find index of the first Fibonacci number with n digits. n = ", end="")
    n = int(input())
    generateFibonacciIndexes()
    print("The first Fibonacci number with %d digits is at index %d" % (n, fibIndex[n-1]))

if __name__ == "__main__":
    main()
