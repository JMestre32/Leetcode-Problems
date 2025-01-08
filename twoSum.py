class Solution(object):
    def twoSum(self, nums, target):
        myDict = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in myDict:
                return [myDict[diff], i]
            myDict[n] = i
        return
    
# Topics/Data Structures: 
# 1. Dictionaries

# Pitfalls:
# 1. enumerate is NOT tricky, all it does is allow us to get both an index and a value for each item in nums
# 2. We are checking for the difference in our dictionary, but when adding to the dictionary we ARE ADDING THE VALUE FROM NUMS (NOT myDict[diff] = i)
# 3. in line 8, we are returning myDict[diff] and i NOT myDict[diff] and myDict[i], this is because myDict[i] does not correspond to the index we found the answer at. 