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

from p3 import primefactors
from collections import Counter
from functools import reduce

# Find the smallest positive integer that is evenly divisible by all of
# the numbers from 1-20.

# X divides Y iff the prime factors of Y are a super-multiset of the prime
# factors of X. So, we find the intersection of the prime factors of each
# of 1-20, and take the product.

def getanswer():
    answer = Counter()
    for div in range(1,21):
        for factor, count in Counter(primefactors(div)).items():
            answer[factor] = max(answer[factor], count)
    answerprod = reduce(lambda x,y: x*y, answer.elements())
    return answerprod

if __name__ == "__main__":
    print(getanswer())
