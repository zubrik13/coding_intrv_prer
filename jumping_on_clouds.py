#!/bin/python3

"""
There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal 
to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps 
it will take to jump from the starting postion to the last cloud. 
It is always possible to win the game.
For each game, you will get an array of clouds numbered  if they are safe 
or  if they must be avoided.
"""


import math
import os
import random
import re
import sys

def jumpingOnClouds(n, c):
    dist = n - 1
    jumps = 0
    step = 0

    while(step < dist):
        if (step + 2 <= dist and c[step + 2] == 0):
            step += 2
            jumps += 1
        elif(step + 1 <= dist and c[step + 1] == 0):
            step += 1
            jumps += 1    
        
    return jumps


# n = int(input())
# c = list(map(int, input().rstrip().split()))


c = [0, 0, 0, 0, 1, 0]
n = 6


result = jumpingOnClouds(n, c)
print(result)