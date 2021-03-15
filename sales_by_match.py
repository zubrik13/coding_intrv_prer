#!/bin/python3


"""
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example 
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color  and one of color 1. 
There are three odd socks left, one of each color 2. 
The number of pairs is 2.
"""

import math
import os
import random
import re
import sys
from collections import Counter


def sockMerchant(n, ar):
    '''Step-by-step method'''
    d = {}
    # d = dict(Counter(ar))
    counter = 0
    for key in ar:
        if key not in d.keys():
            d[key] = 1
        else:
            d[key] += 1
    
    for value in d.values():
        pairs = value // 2
        if pairs > 0:
            counter += pairs 
            
    return counter                 


"""
def sockMerchant(n, ar):
    '''Cheater method'''
    socks_num = Counter(ar).values()
    counter = 0
    
    for item in socks_num:
        pairs = item // 2
        if pairs > 0:
            counter += pairs 
            
    return counter 
"""

# n = int(input())

# ar = list(map(int, input().rstrip().split()))

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)
print(result)    
    
    
