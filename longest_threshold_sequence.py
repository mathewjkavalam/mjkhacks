#!/usr/bin/python3
def findLongest(hours,x):
    return permu(hours,x,0)

def permu(hours,x,count):
    if type(hours) == type([]) and len(hours) >  0:
        if hours[0] >= x:
            return max( permu(hours[1:],x,count+1), count)
    if( len(hours) > 0):
        return max( permu(hours[1:],x,0), count)
    else:
        return count
print( findLongest([4,7,5,1,9,8,0,0,10,10,10,4,0,3],5 ) )