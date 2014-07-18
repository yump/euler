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

import sys
import collections
import itertools

# 1. The best sum from a node is the value at that node plus the maximum
#    of the best sums from the two nodes below.
# 2. The best sum from a node with nothing below is it's own value.

# Induce.

# Unfortunately, I had originally though I was going to need easy access
# to the nodes above, so I wrote a directed graph class.  Alas, I did
# not realize how simple the solution was until I tried to figure out
# how to turn the input file into a directed graph.

def slidewin(iterable, length):
    """Sliding window generator."""
    it = iter(iterable)
    window = collections.deque(itertools.islice(it,length), maxlen=length)
    yield window
    for x in it:
        window.append(x)
        yield window

def getanswer(filename):
    #slurp
    with open(filename) as datafile:
        triangle = [
                    [ int(x) for x in line.split() ]
                    for line in datafile.read().splitlines() 
                   ]
    # initial state
    below = [0 for i in range(1 + len(triangle[-1]))]
    #calculate
    for row in reversed(triangle):
        below = [ row[i]+max(pair) for i,pair in enumerate(slidewin(below,2)) ]
    return below[0]


if __name__ == "__main__":
    # Run me on the data file
    print(getanswer(sys.argv[1]))
