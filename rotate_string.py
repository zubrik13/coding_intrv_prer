"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving 
the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' 
after one shift on A. Return True if and only if A can 
become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""

def rotateString_s(A, B):
    """string manipulation"""
    if len(A) == 0 and len(B) == 0:
        return True
    if len(A) == 0 and len(B) == 1:
        return False
    
    temp = A + A[0]

    size =  len(A) - 1

    for i in range(size):
        if temp[i+1:] == B:
            return True
        else:
            temp += A[i+1]
      
    return False


def rotateString(A, B):
    return len(A) == len(B) and B in A+A
        
        
s1 = 'abcde'
s2 = 'cdeab'
s3 = ''
s4 = 'b'

print rotateString_s(s1, s2)
print rotateString_s(s3, s4)
