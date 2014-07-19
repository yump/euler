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

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).  If d(a) = b and d(b) = a, where 
a != b, then a and b are an amicable pair and each of a and b are 
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from numerology import divisors

amicable_cache = set()

def isamicable(a):
    if a in amicable_cache:
        return True
    if a < 2:
        # 0 itself cannot be factored, and the sum of 1's proper
        # divisors is 0. 
        return False
    b = sum(divisors(a)) - a
    if (a != b) & (sum(divisors(b)) - b == a):
        amicable_cache.update((a,b))
        return True
    else:
        return False
    
def getanswer():
    return sum(i for i in range(10000) if isamicable(i))

if __name__ == "__main__":
    print(getanswer())
