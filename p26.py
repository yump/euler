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
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    1/2  =  0.5
    1/3  =  0.(3)
    1/4  =  0.25
    1/5  =  0.2
    1/6  =  0.1(6)
    1/7  =  0.(142857)
    1/8  =  0.125
    1/9  =  0.(1)
    1/10 =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

from itertools import count

def reciprocal_cyclelength(integer, base=10):
    history = {} # intermidiate quotients -> number of steps when first seen
    state = 1 # initial dividend
    for nsteps in count():
        state = state*base % integer
        if state == 0:
            return 0 # quotient is nonrepeating
        elif state in history:
            return nsteps - history[state]
        else:
            history[state] = nsteps

def getanswer():
    length, div = max( (reciprocal_cyclelength(i), i) for i in range(1,1000) )
    return "length: {} div: {}".format(length,div)

if __name__ == "__main__":
    print(getanswer())
