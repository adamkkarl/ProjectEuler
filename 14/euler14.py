#!/bin/python3

__author__ = "Adam Karl"
"""The Collatz sequence is defined by:
if n is even, divide it by 2
if n is odd, triple it and add 1
given N, which number less than or equal to N has the longest chain before hitting 1?"""
#https://projecteuler.net/problem=14
#April 2018

MAXIMUM = 0
steps = []
answers = []

def update(n):
    """Update the array  so that now has at least an answer for key=n"""
    """likely will also fill in additional step lengths"""
    if n == 1: #base case 1
        return 0

    s = 0  
    if n < MAXIMUM: #should have a n answer in this spot
        if steps[n] != None: #already know answer for this spot
            return steps[n]
        
        if n % 2 == 0:
            s = 1 + update(n>>1)
        else:
            s = 1 + update(3*n + 1)
        steps[n] = s #fill in an answer
    else: #calculate on the fly
        if n % 2 == 0:
            s = 1 + update(n>>1)
        else:
            s = 1 + update(3*n + 1)
    return s
        
def populateCollatz():
    """populates collatz steps array up to n"""
    global steps
    global answers
    steps = [None]*(MAXIMUM)
    answers = [0]*(MAXIMUM)
    steps[0] = 1
    steps[1] = 0
    for i in range(1, MAXIMUM):
        if steps[i] == None:
            update(i)
            
def populateAnswers():
    """Using the array of number of steps for N, produce an array of the value that produces
    the maximum # of steps less than of equal to N (in case of a tie use the larger number).
    Using this method we only have to check an array for the maximum 1 time rather than for every
    test case N"""
    max_steps = 0
    max_index = 0
    for i in range(MAXIMUM):
        if max_steps <= steps[i]:
            max_steps = steps[i]
            max_index = i
        answers[i] = max_index
        
def main():
    global MAXIMUM
    print("Which number under __ produces the longest collatz sequence? ", end="")
    MAXIMUM = int(input()) + 1
    populateCollatz()
    populateAnswers()
    print("%d produces the longest sequence" % answers[MAXIMUM-1])

if __name__ == "__main__":
    main()
