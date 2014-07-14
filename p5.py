#!/usr/bin/env python3

from p3 import primefactors
from collections import Counter
from functools import reduce

# Find the smallest positive integer that is evenly divisible by all of
# the numbers from 1-20.

# X divides Y iff the prime factors of Y are a super-multiset of the prime
# factors of X. So, we find the intersection of the prime factors of each
# of 1-20, and take the product.

def getanswer():
    answer = Counter()
    for div in range(1,21):
        for factor, count in Counter(primefactors(div)).items():
            answer[factor] = max(answer[factor], count)
    answerprod = reduce(lambda x,y: x*y, answer.elements())
    return answerprod

if __name__ == "__main__":
    print(getanswer())
