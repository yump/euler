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
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) +
41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces
80 primes for the consecutive values n = 0 to 79. The product of the
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

from numerology import isprime
from itertools import count, product

def nprimes_quadratic(a, b):
    for n in count():
        if not isprime(n**2 + a*n + b):
            return n

def getanswer():
    mostprimes, bestproduct = max(
            (nprimes_quadratic(a,b), a*b) 
            for a,b in product(*[range(-999,1000)]*2)
            )
    return bestproduct

if __name__ == "__main__":
    print(getanswer())
