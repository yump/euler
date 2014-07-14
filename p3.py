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

import itertools

def primefactors(n):
    bigpart = n
    for div in itertools.chain([2],range(3,n,2)):
        if div**2 > bigpart:
            break
        while bigpart % div == 0:
            yield div
            bigpart = bigpart // div
    if bigpart != 1:
        yield bigpart

def getanswer():
    return sorted(primefactors(600851475143))[-1]

if __name__ == "__main__":
    print(getanswer())
