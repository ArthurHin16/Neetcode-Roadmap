hashmap = set(nums)
    longest_sequence = 0
    for num in nums:
        if (num - 1) not in hashmap:
            length = 0
            while (num + length) in hashmap:
                length += 1
        longest_sequence = max(longest_sequence, length)
    return longest_sequence