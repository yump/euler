#!/usr/bin/env python3
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

from numerology import primefactors, prod, power_set
import itertools
from collections import Counter

def trinums():
    n = 0
    for i in itertools.count(1):
        n += i
        yield n

def numfactors(n):
    nfactors = 0
    factorization = Counter(primefactors(n))
    for subset in power_set(factorization.keys()):
        # Each subset of the prime factorization contributes a number of
        # divisors equal to the product ot the multiplicities of the factors
        # in the subset.

        # For example:
        # 12 -> (2,2,3) -> ((),(2),(3),(2,3)) -> ((1),(2,4),(3),(6,12))
        nfactors += prod(factorization[k] for k in subset)
    return nfactors
    
def getanswer():
    return next(n for n in trinums() if numfactors(n) > 500)

if __name__ == "__main__":
    print(getanswer())
