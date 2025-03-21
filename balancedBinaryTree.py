# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

#  Conceptual Answer:

# You're gonna want to use a depth-first search and start from the bottom leaf node and determine if that node is balanced, it will have a height of 0 since the left and right nodes are nonexistent.
# At each step up you'll want to return a Tuple, a boolean stating if the subtree is balanced and the height of that subtree. You find the height by taking the max height of the left and right subtrees. 
# To determine if a subtree is balanced, you must ensure that the root's subtrees are balanced, and that the difference in height in the left and right subtrees is no more than 1. 
# Once you've reached the root node, return the first index of the function dfs(root), this will start the entire bottom-up approach. 