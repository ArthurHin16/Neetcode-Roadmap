"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def contains_duplicate(nums):
    numbers = set()
    for num in nums:
        if num not in numbers:
            numbers.add(num)
        else:
            return True
    return False

