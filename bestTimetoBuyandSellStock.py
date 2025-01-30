from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1

        maxP = 0

        while right < len(prices):

            if prices[left] < prices[right]:

                profit = prices[right] - prices[left]

                maxP = max(maxP, profit)
            
            else:
                left = right
            right += 1
        
        return maxP

#Topics:

# Two Pointer

# Conceptual Answer

# You want to have two pointers, left and right, to hold the index of the most profitable day essentially. So, when the left pointer is less than the right, use a profit variable
# to compare profit to maxP (which is initialized to 0). If this never happens, then right is incremented at each loop until no profit is found and 0 is returned as maxP, meaning
# there is no way to profit given the array. 