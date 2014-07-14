#!/usr/bin/env python3

import itertools

def primefactors(n):
    bigpart = n
    for div in itertools.chain([2],range(3,n,2)):
        if div**2 > bigpart:
            break
        while bigpart % div == 0:
            yield div
            bigpart = bigpart // div
    if bigpart != 1:
        yield bigpart

def getanswer():
    return sorted(primefactors(600851475143))[-1]

if __name__ == "__main__":
    print(getanswer())
