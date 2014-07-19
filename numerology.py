# Copyright (C) 2014 Russell Haley
# 
# This file is part of euler.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import itertools
import math

def power_set(seq):
    """
    Generator which yields all subsets of a sequence.
    """
    seq = tuple(seq)
    for size in range(len(seq)+1):
        for combo in itertools.combinations(seq,size):
            yield combo

def primefactors(n):
    """
    Generator which yields the prime factors of n.
    """
    bigpart = n
    for div in itertools.chain([2],range(3,n,2)):
        if div**2 > bigpart:
            break
        while bigpart % div == 0:
            yield div
            bigpart = bigpart // div
    if bigpart != 1:
        yield bigpart

def isprime(n):
    """Test if n is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    for div in itertools.chain([2],range(3, int(math.sqrt(n))+1, 2)):
        if n % div == 0:
            return False
    return True

def primes(n):
    """Yield the first n primes."""
    nprimes = 0
    for i in itertools.count(1):
        if isprime(i):
            nprimes += 1
            yield i
        if nprimes == n:
            break

def prod(seq):
    """
    Calculate the product of a sequence.
    """
    result = 1
    for x in seq:
        result *= x
    return result
