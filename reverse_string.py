"""
Write a function that reverses a string. 
The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array 
in-place with O(1) extra memory.

You may assume all the characters consist of printable 
ascii characters.
"""
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1



def reverse_in_place(lst):      # Declare a function
    size = len(lst)             # Get the length of the sequence
    hiindex = size - 1
    itrs = size/2                # Number of iterations required
    for i in range(0, itrs):    # i is the low index pointer
        temp = lst[hiindex]     # Perform a classic swap
        lst[hiindex] = lst[i]
        lst[i] = temp
        hiindex -= 1            # Decrement the high index pointer
    print "Done!"


l = ["h","e","l","l","o"]
# reverse_in_place(l)
Solution().reverseString(l)

print l






