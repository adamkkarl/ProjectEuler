#!/bin/python3

__author__ = "Adam Karl"
#https://projecteuler.net/problem=38

def repeatsDigits(n):
    """Return True if n has repeat digits or a 0, True otherwise"""
    s = str(n)
    alreadySeen = [True]
    for i in range(9):
        alreadySeen.append(False)
    for c in s:
        if(alreadySeen[int(c)]):
            return True
        else:
            alreadySeen[int(c)] = True
    return False
    
def main():
    largest = 0
    for i in range(1, 333334): #3n must be only 9 digits
        prodList = []
        chars = 0
        mul = 1
        while(chars < 9):
            p = str(i*mul)
            prodList.append(p)
            chars += len(p)
            mul += 1

        if (chars == 9):
            test = "".join(prodList)
            if (not repeatsDigits(test) and int(test) > largest):
                largest = int(test)
    print("The largest pandigital product made this way is %d" % largest)

if __name__ == "__main__":
    main()
