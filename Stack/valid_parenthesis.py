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

    for p in s:
        if p not in hashmap:
            stack.append(p)
        else:
            curr = hashmap[p]
            if not stack or stack[-1] != curr:
                return False
            stack.pop()

    return True if not stack else False


s = "()"
print(valid_parenthesis(s))
