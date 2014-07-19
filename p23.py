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
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

from numerology import divisors
from itertools import combinations_with_replacement

TOPRANGE = 28124

def is_abundant(n):
    return( sum(divisors(n)) - n > n )

def getanswer():
    # As stated, all integers > 28123 can be written as a sum of two
    # abundant numbers, so we only need to consider 28123 and below.
    abundant_numbers = [ i for i in range(1,TOPRANGE) if is_abundant(i) ]
    abundant_sums = set( 
                         x+y for x,y in 
                         combinations_with_replacement(abundant_numbers,2)
                         if x+y < TOPRANGE
                       )
    # Sum numbers that are not abundant sums
    return sum(i for i in range(TOPRANGE) if i not in abundant_sums)


if __name__ == "__main__":
    print(getanswer())
