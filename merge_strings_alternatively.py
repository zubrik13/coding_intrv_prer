"""
You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. 
If a string is longer than the other, append 
the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""
word1 = "abc" 
word2 = "pqrst"

# lst1 = list(word1)
# lst2 = list(word2)

# print lst1, lst2
l1 = len(word1)
l2 = len(word2)
d = abs(l1 - l2) 

if l1 < l2:
    lst1 = list(word1)
    lst2 = list(word2[:l1])
    delta = word2[-d:]
elif l1 > l2:
    lst1 = list(word1[:l2])
    lst2 = list(word2)
    delta = word1[-d:]
else:
    lst1 = list(word1)
    lst2 = list(word2)
    delta = ""

out = ""

for i, j in zip(lst1, lst2):
    out += i
    out += j

print out + delta