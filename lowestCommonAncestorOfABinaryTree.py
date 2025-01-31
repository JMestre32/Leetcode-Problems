#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        

# Topics:

# Binary tree

# Conceptual Answer:
# Start at the root node and use a variable cur to track the current node. If both p and q are greater than cur.val, move right. 
# If both are smaller, move left. As soon as p and q are no longer on the same side (or one of them is the current node),
# cur is the lowest common ancestor, so return it.