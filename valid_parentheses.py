"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

def bracket_checker(s):

    opn = ["[","{","("] 
    clos = ["]","}",")"]

    brackets = dict(zip(clos, opn))
    stack = []

    for i in s:
        if i in opn:
            stack.append(i)
        elif i in clos:
            if stack[-1] == brackets[i]:
                stack.pop()
            elif len(stack) == 0:
                return False           
            else:
                return False

    return len(stack) == 0


def bracker_checker_simple(s):

    counter = 0

    for i in s:
        if i in opn:
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False

    return counter == 0



s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
s6 = "(())(()))"

print bracket_checker(s4)
print bracket_checker(s5)


