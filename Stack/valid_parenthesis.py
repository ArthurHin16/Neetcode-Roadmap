"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def valid_parenthesis(s):
    hashmap = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for c in s:
        if c not in hashmap:
            stack.append(c)
        else:
            curr = hashmap[c]
            if not stack or curr != stack[-1]:
                return False
            stack.pop()

    return True if not stack else False


s = "]"
print(valid_parenthesis(s))

# curr = (