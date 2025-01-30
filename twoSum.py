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
# 4. In line 9, assuming we are at index 0 and the first value is 2, we want our dict to look like 2 : 0, we are not doing myDict[diff] = i, then we would have 7 : 1 which isn't what we want. 

# Conceptual Answer:

# Use enumerate to obtain an index and the actual value at i using the variable 'n' in nums. 
# create your own dictionary that will hold each value in nums and their respective index in nums
# use a variable, diff, to see if it is already in your created dictionary. If diff is not in your dictionary, add 'n' to the dictionary with a value of 'i'.
# repeat until you find a matching combination then return it using []. 