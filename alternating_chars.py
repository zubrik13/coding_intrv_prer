"""
You are given a string containing characters  and  only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
"""
s = 'AAABBB'

min_num = 0
last_char = len(s) - 1


for i in range(last_char):
    if s[i] == s[i+1]:
        min_num += 1


print(min_num)

