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

import datetime

SUNDAY = 6

def getanswer():
    date = datetime.datetime(1901,1,1)
    increment = datetime.timedelta(days=1)
    stop = datetime.datetime(2000,12,31) + increment
    nsundays = 0
    while date < stop:
        if (date.day == 1) & (date.weekday() == SUNDAY):
            nsundays += 1
        date += increment
    return nsundays

if __name__ == "__main__":
    print(getanswer())
