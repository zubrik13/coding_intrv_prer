"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith 
position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

strng = []

for letter in s:
    strng.append(letter)

d = dict(zip(indices, strng))

# print(d)
out = ''
for i in sorted(d):
    out += d[i]

print(out)

