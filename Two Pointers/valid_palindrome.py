# Given a string s, return true if it is a palindrome, or false otherwise.
"""
To solve this problem we can use many approaches, but to solve this problem we will be using the two pointers technique. 
The valid characters are numbers an letters. We can use the following functions to verify if those conditions are meet:
- isalpha(): Returns True if the digit is a letter, otherwise returns False.
- isalnum(): Returns True if the digit is a letter or a number, otherwise returns False.
- isdigits(): Returns True if the digit is a number, otherwise returns False.

"""

#Solution with two pointers
def valid_palindrime(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

#Solution using Slicing Python Notation
def valid_palindrome_slicing(s):
    string = ""
    for c in s:
        if c.isalnum():
            string += c.lower()
    return string == string[::-1]


s = "A man, a plan, a canal: Panama"
print(valid_palindrime(s))
print(valid_palindrome_slicing(s))