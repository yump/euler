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

import numpy as np
import functools
import itertools

# All pythagorean triples are primitive triples or multiples of primitive
# triples, where a primitive triple is a triple where the members share
# no common factors. All primitive triples form a ternary tree rooted at
# (3,4,5), where edges are traversed by matrix multiplication with one
# of 3 generating matrices.

# See http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

ROOT_TRIPLE=np.array((3,4,5))

GEN_MATRICES=(
        np.array(((1,-2,2),(2,-1,2),(2,-2,3))),
        np.array(((1,2,2),(2,1,2),(2,2,3))),
        np.array(((-1,2,2),(-2,1,2),(-2,2,3)))
        )

@functools.lru_cache(maxsize=32)
def prim_pythag(index):
    """
    Produce the index'th primitive pythagorean triple. This function
    implements a mapping from integers >0 to the set of primitive
    pythagorean triples.
    """
    if index == 0:
        return ROOT_TRIPLE
    else:
        edge = index % 3
        parent = (index-1) // 3
        return GEN_MATRICES[edge].dot(prim_pythag(parent))

def getanswer():
    """
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    for i in itertools.count():
        triple = prim_pythag(i)
        # The triple we want might not be primitive.
        if 1000 % sum(triple) == 0:
            triple *= 1000 // sum(triple) # Convert to non-primitive if needed
            return triple, functools.reduce(lambda x,y: x*y, triple)

if __name__ == "__main__":
    print(getanswer())

