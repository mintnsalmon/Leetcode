
# coding: utf-8

# In[ ]:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root == None:
            return None
        
        if root in nodes:
            return root
        
        left =  self.lowestCommonAncestor(root.left, nodes)
        right = self.lowestCommonAncestor(root.right, nodes)
        
        if right == None:
            return left
        elif left == None:
            return right
        else:
            return root

