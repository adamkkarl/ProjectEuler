#!/bin/python3

__author__ = "Adam Karl"
"""Given a number, write it to words"""
#https://projecteuler.net/problem=17
#April 2018


def parseOneDigit(n):
    """Given a single digit 1-9, return its name in a word"""
    if n == 1:
        return "One "
    elif n == 2:
        return "Two "
    elif n == 3:
        return "Three "
    elif n == 4:
        return "Four "
    elif n == 5:
        return "Five "
    elif n == 6:
        return "Six "
    elif n == 7:
        return "Seven "
    elif n == 8:
        return "Eight "
    elif n == 9:
        return "Nine "
    return ""

def parseTwoDigits(n,m):
    """Given a 2 digit number with digits nm, return its name in a word"""
    if n == 0:
        return parseOneDigit(m)
    elif n == 1:
        if m == 0:
            return "Ten "
        elif m == 1:
            return "Eleven "
        elif m == 2:
            return "Twelve "
        elif m == 3:
            return "Thirteen "
        elif m == 4:
            return "Fourteen "
        elif m == 5:
            return "Fifteen "
        elif m == 6:
            return "Sixteen "
        elif m == 7:
            return "Seventeen "
        elif m == 8:
            return "Eighteen "
        elif m == 9:
            return "Nineteen "
    elif n == 2:
        return "Twenty " + parseOneDigit(m)
    elif n == 3:
        return "Thirty " + parseOneDigit(m)
    elif n == 4:
        return "Forty " + parseOneDigit(m)
    elif n == 5:
        return "Fifty " + parseOneDigit(m)
    elif n == 6:
        return "Sixty " + parseOneDigit(m)
    elif n == 7:
        return "Seventy " + parseOneDigit(m)
    elif n == 8:
        return "Eighty " + parseOneDigit(m)
    elif n == 9:
        return "Ninety " + parseOneDigit(m)
    
def parseThreeDigits(m, n, p):
    s = parseOneDigit(m)
    if s != "":
        s += "Hundred "
        if (n>0 or p>0):
            s += "and "
    s += parseTwoDigits(n,p)
    return s
    

def parseWholeNumber(arr):
    titles = ["", "Thousand ", "Million ", "Billion ", "Trillion "]
    string = ""
    titleIndex = 0
    while len(arr) > 0:
        length = len(arr)
        a,b,c = 0,0,0
        if length >= 3: #a,b,c all have values
            a = arr[-3]
            b = arr[-2]
            c = arr[-1]
        elif length == 2:
            b = arr[-2]
            c = arr[-1]
        else:
            c = arr[-1]

        threeDigitString = parseThreeDigits(a,b,c)
        if threeDigitString != "": #000 would give ""
            string = threeDigitString + titles[titleIndex] + string
        titleIndex += 1
        if length < 4:
            arr = []
        else:
            arr = arr[:-3]
    return string

def lettersInString(s):
    """return the number of non-whitespace or hyphen characters in a string"""
    ret = 0
    for c in s:
        if (c!=' ' and c!=' '):
            ret += 1
    return ret


def main():
    print("Add the characters of numbers 1 through: ", end="")
    max = int(input())
    sum = 0
    for i in range(1, max + 1):
        digits = []
        for d in str(i):
            digits.append(int(d))
        word = parseWholeNumber(digits)
        sum += lettersInString(word)
    print("%d characters" % sum)

if __name__ == "__main__":
    main()
