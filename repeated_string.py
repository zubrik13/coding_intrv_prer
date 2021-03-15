"""
There is a string, s, of lowercase English letters 
that is repeated infinitely many times. 
Given an integer, n, find and print the number of letter a's 
in the first n letters of the infinite string.
"""

s = "abcac"
n = 14

multiplicator = n // len(s)
count_a = 0
for letter in s:
    if letter == "a":
        count_a += 1


delta = n % len(s)
count_delta_a = 0
if delta != 0:
    sub_s = s[:delta] 
    for letter in sub_s:
        if letter == "a":
            count_delta_a += 1


num_a = multiplicator * count_a + count_delta_a    

print(num_a)