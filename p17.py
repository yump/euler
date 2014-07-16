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

from collections import namedtuple

DIGITS={0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'}

TEENS={10: 'ten',
       11: 'eleven',
       12: 'twelve',
       13: 'thirteen',
       14: 'fourteen',
       15: 'fifteen',
       16: 'sixteen',
       17: 'seventeen',
       18: 'eighteen',
       19: 'nineteen'}

TIES={2: 'twenty',
      3: 'thirty',
      4: 'forty',
      5: 'fifty',
      6: 'sixty',
      7: 'seventy',
      8: 'eighty',
      9: 'ninety',}

def select_digits(integer, lowplace, highplace=None):
    """
    Get the value of the (highplace,lowplace] subsequence in the base 10
    representation of an integer.
    """    
    if highplace is None:
        highplace = lowplace+1
    return (integer // 10**lowplace) % 10**(highplace - lowplace)

def num2eng_under_1k(integer, use_and=True):
    assert integer < 1000
    result = []
    hundreds = select_digits(integer,2)
    tens = select_digits(integer,1)
    ones = select_digits(integer,0)
    # Handle hundreds
    if hundreds > 0:
        result.append(DIGITS[hundreds])
        result.append('hundred')
        if (select_digits(integer,0,2) != 0) & use_and:
            result.append('and')
    # Handle tens and ones
    if (tens > 1) & (ones != 0):
        result.append(TIES[tens] + '-' + DIGITS[ones])
    elif (tens > 1) & (ones == 0):
        result.append(TIES[tens])
    elif tens == 1:
        result.append(TEENS[10*tens + ones])
    elif (tens == 0) & (ones != 0):
        result.append(DIGITS[ones])
    elif (tens == 0) & (ones == 0):
        pass
    else:
        # All cases should be covered
        assert False 
    return " ".join(result)

Block = namedtuple('Block', ['name','low','high'])

BLOCKS = (Block('thousand',3,6),
          Block('million',6,9),
          Block('billion',9,12),
          Block('trillion',12,15))

def num2eng(integer, use_and=True):
    result = []
    for block in reversed(BLOCKS):
        segment = select_digits(integer, block.low, block.high)
        if segment > 0:
            result.append(num2eng_under_1k(segment, use_and)+' '+block.name)
    segment = select_digits(integer,0,3)
    if segment > 0:
        result.append(num2eng_under_1k(segment, use_and))
    if use_and:
        return ' and '.join(result)
    else:
        return ' '.join(result)

def nchars_in_eng_number(integer):
    return len([l for l in num2eng(integer) if l not in {' ','-'}])

def getanswer():
    return sum(nchars_in_eng_number(i) for i in range(1,1001))

if __name__ == "__main__":
    print(getanswer())
