def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        midd = (l + r)//2
        if nums[midd] == target:
            return midd
        elif nums[midd] > target:
            r -= 1
        else:
            l += 1
    return -1
