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

from scipy.misc import comb
def npaths_across_grid(gridsize):
    """
    Find the number of paths through a grid from one corner to the
    opposite corner..

    Paramaters
    ----------
    gridsize : 2-tuple
        The shape of the grid.  First element is number of rows, second
        is number of columns.

    Returns
    ------
    out : int
        The number of paths through the grid from one corner to the
        opposite corner.
    """
    rows, cols = gridsize
    # Consider the lattice of nodes that make up the grid, which is 1 
    # larger than the grid in each dimension. Starting from the top-left
    # corner, there are cols+1 opportunities for the path to go down,
    # and the total number of down edges must equal the number of rows.
    # The problem is thus equivalent to dividing rows objects into 
    # cols+1 bins.

    # Such a division is equivalent to inserting nbins-1 (i.e., cols)
    # dividers into a sequence of rows objects.  This is further
    # equivalent to choosing nbins-1 objects from a sequence of 
    # rows+nbins-1 objects and turning them into dividers.

    return(comb(rows+cols, cols, exact=True))

def getanswer():
    assert npaths_across_grid((2,2)) == 6
    return npaths_across_grid((20,20))

if __name__ == "__main__":
    print(getanswer())
