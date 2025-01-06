class Solution(object):
    def twoSum(self, nums, target):
        myDict = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in myDict:
                return [myDict[diff], i]
            myDict[n] = i
        return