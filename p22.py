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
Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def alphavalue(string):
    normed = string.lower()
    return sum( char.encode('ascii')[0] - 96 for char in normed )

def getanswer():
    #slurp
    with open("names.txt") as datafile:
        text = datafile.read()
    names = [ n.strip('"') for n in text.split(',') ]
    total = 0
    for pos, name in enumerate(sorted(names)):
        total += alphavalue(name) * (pos + 1)
    return total

if __name__ == "__main__":
    print(getanswer())
