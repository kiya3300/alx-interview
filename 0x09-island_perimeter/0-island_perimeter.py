#!/usr/bin/python3
"""function  returns the perimeter of the island described in grid"""
    
def island_perimeter(grid):
    """
    grid: is a list of list of integers:
            0 represents water
            1 represents land
    """
    x = len(grid)
    y = len(grid[0])
    if(x==0 or y==0):
        return 0
    else:
        perimeter = 0
        for i in range(0,x):
            for j in range(0,y):
                if(grid[i][j]==1):
                    if(i-1<0):
                        perimeter = perimeter+1
                    elif(grid[i-1][j]==0):
                        perimeter = perimeter+1
                    if(i+1==x):
                        perimeter = perimeter+1
                    elif(grid[i+1][j]==0):
                        perimeter = perimeter+1
                    if(j-1<0):
                        perimeter = perimeter+1
                    elif(grid[i][j-1]==0):
                        perimeter = perimeter+1
                    if(j+1==y):
                        perimeter = perimeter+1
                    elif(grid[i][j+1]==0):
                        perimeter = perimeter+1
        return perimeter
