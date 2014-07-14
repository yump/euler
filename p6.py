#!/usr/bin/env python3

def getanswer():
    sumsq = sum( x**2 for x in range(1,101) )
    sqsum = sum(range(1,101))**2
    return abs(sumsq-sqsum)

if __name__ == "__main__":
    print(getanswer())
