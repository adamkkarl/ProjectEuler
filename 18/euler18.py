#!/bin/python3

__author__ = "Adam Karl"
"""Find the maximum sum from following a path down a triangle of numbers"""
#https://projecteuler.net/problem=18

tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def maximize(pyramid):
    """Recursively find the sum of the maximum path for the pyramid"""
    row = len(pyramid) - 2 #last row remains unchanged
    while row >= 0:
        numItems = row + 1
        for i in range(numItems):
            maxNext = pyramid[row+1][i]
            if maxNext < pyramid[row+1][i+1]:
                maxNext = pyramid[row+1][i+1]
            pyramid[row][i] = pyramid[row][i] + maxNext
        row -= 1
    return pyramid[0][0]

def main():
    print("Finding max sum for\n%s" % tri)

    pyr = []
    for row in tri.split("\n"):
        line = row.split(" ")
        line = list(map(int, line))
        pyr.append(line)
    print("Max sum = %d" % maximize(pyr))


if __name__ == "__main__":
    main()
