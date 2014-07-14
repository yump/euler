#!/usr/bin/env pythoh3

from p3 import primefactors
from collections import deque
import itertools
import math

#This is an unbelievably naive solution.  I have a fast CPU.

def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for div in itertools.chain([2],range(3, int(math.sqrt(n))+1, 2)):
        if n % div == 0:
            return False
    return True

def natural_numbers():
    i=1
    while True:
        yield i
        i+=1

def primes(n):
    nprimes = 0
    for i in natural_numbers():
        if isprime(i):
            nprimes += 1
            yield i
        if nprimes == n:
            break
        
if __name__ == "__main__":
    # 10001'st prime
    answer = deque(primes(10001), maxlen=1)[0]
    print(answer)