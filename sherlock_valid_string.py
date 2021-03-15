from collections import Counter

# s = 'abcdefghhgfedecba'
s = 'aabbcd'
# s = 'aaabbbcccd'
# s = 'aaaabbcc'

d = {}

for char in s:
    if char not in d.keys():
        d[char] = 1
    else:
        d[char] += 1

most_frequent = Counter(d.values()).most_common(1)[0][0]
# most_frequent = Counter(d.values()).most_common()

max_val = max(d.values())
min_val = min(d.values())

print(most_frequent)

outliers = 0

for i in d.values():
    if i != most_frequent:
        outliers += 1

print(outliers)

if outliers == 0:
    print("YES")
elif (outliers == 1) and ((max_val - most_frequent) == 1):
    print("YES")
# elif (outliers == 1) and ((out_val + 1) == most_frequent):
#     print("YES")

else:
    print("NO")

