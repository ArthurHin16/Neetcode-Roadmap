"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

def longest_consecutive_sequence(nums):
    hashmap = set(nums)
    longest_sequence = 0
    for num in nums:
        if (num - 1) not in hashmap:
            length = 0
            while (num + length) in hashmap:
                length += 1
            longest_sequence = max(longest_sequence, length)
    return longest_sequence





nums = [0, -1]
print(longest_consecutive_sequence(nums))