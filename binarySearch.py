class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else: 
                return m
        
        return -1

# Topics
# Binary Search

# Conceptual Answer:
# We are already given a sorted list.
# Binary search, in this context, means we look at the midway point, m, of two pointers, l (equal to 0) and r (equal to length of the list) and compare it to the target, 
# depending on what that value at the midway point is (less or more than the target), we cut the half of the list that the target CANNOT be in 
# (i.e. if the target is 9 and we are at 3, we discard all values below 3). Then, we set the left pointer equal to m + 1 and repeat until we find the target.
# [-1, 0, 3, 5, 9, 12] -> [5, 9, 12] -> return m

# 1. l = 0, r = 5, m = 2
# 2. l = 3, r = 5, m = 4
# return m

# Time complexity: 
# O(log n)
# We either find the target or at least eliminate half of the possibilities.
# Assuming a list of length 16 (16 -> 8 -> 4 -> 2 -> 1)
# If we have a while loop, we can only run this as many times as we can divide the length of the list by 2. 
# In other words this runs in log2n read as log base 2n