"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
"""
def valid_anagram(s, t):

    s_letters = {}
    t_letters = {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        s_letters[s[i]] = 1 + s_letters.get(s[i], 0)
        t_letters[t[i]] = 1 + t_letters.get(t[i], 0)

    return s_letters == t_letters

s = "rat"
t = "car"

print(valid_anagram(s,t))