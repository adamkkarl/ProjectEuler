#!/bin/python3

import sys

def down_right(x, y, grid):
    """Test products in \ line starting with top left. return 0 if out of bounds"""
    if x + 3 > 19 or y + 3 > 19:
        return 0
    prod = 1
    for i in range(4):
        prod *= grid[x+i][y+i]
    return prod

def down_left(x, y, grid):
    """Test products in / line starting with top right. return 0 if out of bounds"""
    if x - 3 < 0 or y + 3 > 19:
        return 0
    prod = 1
    for i in range(4):
        prod *= grid[x-i][y+i]
    return prod

def right(x, y, grid):
    """Test products in -- line starting with leftmost. return 0 if out of bounds"""
    if x + 3 > 19:
        return 0
    prod = 1
    for i in range(4):
        prod *= grid[x+i][y]
    return prod

def down(x, y, grid):
    """Test products in | line starting with topmost. return 0 if out of bounds"""
    if y + 3 > 19:
        return 0
    prod = 1
    for i in range(4):
        prod *= grid[x][y+i]
    return prod

grid = []
for grid_i in range(20):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(grid_t)

max_prod = 0
for x in range(20):
    for y in range(20):
        test = down_right(x, y, grid)
        if test > max_prod:
            max_prod = test
            
        test = down_left(x, y, grid)
        if test > max_prod:
            max_prod = test
            
        test = right(x, y, grid)
        if test > max_prod:
            max_prod = test
            
        test = down(x, y, grid)
        if test > max_prod:
            max_prod = test
print(str(max_prod))

        
    
