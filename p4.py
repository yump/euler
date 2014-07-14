#!/usr/bin/env python3

import itertools

def ispalindrome(word):
    return all( word[i] == word[-(i+1)] for i in range(len(word) // 2) )

def palindrome_products(n):
    for x,y in itertools.combinations_with_replacement(range(n),2):
        if ispalindrome(str(x*y)):
            yield x*y

def getanswer():
    return sorted(palindrome_products(1000))[-1]

if __name__ == "__main__":
    print(getanswer())


