# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]: # type: ignore
       if root is None: 
           return None
       
       #swap the children
       tmp = root.left
       root.left = root.right
       root.right = tmp

       self.invertTree(root.left)
       self.invertTree(root.right)
       return root
    

# Topics:
# Binary Trees
# DFS (comlpetely finish traversal of all vertices reachable through that vertex [i.e. traverse left subtree THEN traverse right subtree])
# Recursion

# Conceptual Answer: 
# At the first call of invertTree, swap the left and right nodes. Then, use DFS to recursively call invertTree on the new left branch. Once the left branch reaches a None node,
# recursively call invertTree on the new right branch. What this means is that this process of swapping, then recursively calling happens over and over again until all branches are
# visited and the final inverted binary tree is built and returned to the original call to the invertTree function.  