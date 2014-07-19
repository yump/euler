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
import collections
import math

def power_set(seq, proper=False):
    """
    Generator which yields all subsets of a sequence. If proper is True,
    only yield proper subsets.
    """
    seq = tuple(seq)
    if proper:
        maxsize = len(seq)
    else:
        maxsize = len(seq) - 1
    for size in range(maxsize+1):
        for combo in itertools.combinations(seq,size):
            yield combo

def primefactors(n):
    """
    Get a list of the prime factors of n.
    """
    result = []
    bigpart = n
    for div in itertools.chain([2],range(3,n,2)):
        if div**2 > bigpart:
            break
        while bigpart % div == 0:
            result.append(div)
            bigpart = bigpart // div
    if bigpart != 1:
        result.append(bigpart)
    return result

def proper_divisors(n):
    """
    Generator which yields the proper divisors of n. These are the
    numbers less than n which divide n evenly, including 1.
    """
    # A number is a proper factor of n iff it is a product of a strict
    # subset of n's prime factors. Multiplication commutes, so factors
    # with multiplicity > 1 do not generate unique divisors if they are
    # re-ordered.
    # We collapse the prime factors into a multiset and use the fact 
    # that each prime factor can appear [0,multiplicity] times in the
    # factorization of a proper factor.
    factorization = collections.Counter(primefactors(n))
    subprod_lists = [ 
                       [ fact**power for power in range(mult+1) ]
                       for fact, mult in factorization.items()
                    ]
    for pdiv_facts in itertools.product(*subprod_lists):
        proper_div = prod(pdiv_facts)
        if proper_div != n:
            yield proper_div

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
