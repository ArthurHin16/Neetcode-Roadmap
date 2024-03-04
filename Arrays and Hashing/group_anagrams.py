"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict

def group_anagrams(strs):

    hashmap = defaultdict(list) 
    for s in strs:
        letters = [0] * 26
        for c in s:
            letter = ord(c) - ord('a')
            letters[letter] += 1
        hashmap[tuple(letters)].append(s)
    return hashmap.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))