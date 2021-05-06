"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
each substring contains same number of 'L' and 'R'.
"""

s = "RLRRLLRLRL"

balanced = 0

counter = 0

for i in s:

    if i == "R":
        balanced += 1
    else:
        balanced -= 1
    if balanced == 0:
        counter += 1

print counter


# range(len(s)-1)