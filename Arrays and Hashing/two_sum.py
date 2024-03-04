def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        value = target - nums[i]
        if nums[i] in hashmap:
            return [hashmap[nums[i]], i]
        hashmap[value] = i

nums = [3,2,4]
target = 6
print(two_sum(nums, target))

#3 + 4 = 6
#6 - 3 = 4

"""
{
    6 - 3 = 3: 0
    6 - 2 = 4: 1
    6 - 4 = 2: 3
}
"""