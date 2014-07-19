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
    # Each prime factor can appear [0,multiplicity] times in the prime
    # factorization of a factor of n.
    return prod(mult+1 for mult in factorization.values())
    
def getanswer():
    return next(n for n in trinums() if numfactors(n) > 500)

if __name__ == "__main__":
    print(getanswer())
