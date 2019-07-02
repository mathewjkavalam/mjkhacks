#!/usr/bin/python3

def i(n):
    #n -> n-1
    if int(n-1) >= 0:
        return int(n -1)
    else:
        return "NegativeIndex"

def adjacent(x,y,sizeX,sizeY):
    neighbours = []
    if x-1 > 0:
        neighbours.append( (x-1,y) ) 
    if x+1 <= sizeX:
        neighbours.append( (x+1,y) )
    if y-1 > 0:
        neighbours.append( (x,y-1) )
    if( y+1 <= sizeY ):
        neighbours.append( (x,y+1) )
    return neighbours    


mountain = [[7,2,5],[2,3,0]]

def move(x,y,sizeX,sizeY,grid,visited,lowest=10000):
    visited.append( (x,y) )
    neighbours = adjacent(x,y,sizeX,sizeY)
    if neighbours == []:
        return lowest
    for goX,goY in neighbours:
        heightGo = grid[i(goY)][i(goX)]
        heightNow = grid[i(y)][i(x)]
        if( heightGo <= heightNow ):
            if lowest > heightGo:
                lowest = heightGo
            if (x,y) not in visited:
                move(goX,goY,sizeX,sizeY,grid,visited,lowest)
    return lowest

n = 2
m = 3
for x in range(1,m+1):
    for y in range(1,n+1):
        print( move(x,y,m,n,[[7,2,5],[2,3,0]],[],mountain[i(y)][i(x)]) )        