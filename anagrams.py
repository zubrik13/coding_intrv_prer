"""
A student is taking a cryptography class and has found anagrams to be very useful. 
Two strings are anagrams of each other if the first string's letters can be 
rearranged to form the second string. In other words, both strings must 
contain the same exact letters in the same exact frequency. For example, 
bacdc and dcbac are anagrams, but bacdc and dcbad are not.
The student decides on an encryption scheme that involves two large strings. 
The encryption is dependent on the minimum number of character deletions 
required to make the two strings anagrams. Determine this number.
Given two strings, a and b, that may or may not be of the same length, 
determine the minimum number of character deletions required to make 
a and b anagrams. Any characters can be deleted from either of the strings.
"""

a = 'ceed'
b = 'acbeef'

total_len = len(a) + len(b)

match_counter = 0

c = list(a)
d = list(b)

if len(a) <= len(b):
    for i in c:
        if i in d:
            match_counter += 2
            d.remove(i)
else:
    for i in d:
        if i in c:
            match_counter += 2
            c.remove(i)    

min_num = total_len - match_counter

print(min_num) 