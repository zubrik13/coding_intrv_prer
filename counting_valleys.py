#!/bin/python3

"""
An avid hiker keeps meticulous records of their hikes. 
During the last hike that took exactly <steps> steps, 
for every step it was noted if it was an uphill, U, or a downhill, D step. 
Hikes always start and end at sea level, and each step up or down 
represents a  unit change in altitude. We define the following terms:
A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, 
find and print the number of valleys walked through.
"""


import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    altitude = 0
    valleys = 0
    prev_step = []
    for step in path:
        prev_step.append(step)
        if step == "U":
            altitude += 1
        else:
            altitude -= 1
        if altitude == 0 and prev_step[-1] == "U":
            valleys += 1
    return valleys


# steps = int(input().strip())
# path = input()

steps = 8
path = "UDDDUDUU"

result = countingValleys(steps, path)
print(result)

