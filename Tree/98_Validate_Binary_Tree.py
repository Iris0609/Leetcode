## medium
## tree, dfs
## 48ms, beats 100%
## 14.9mb beats 100%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        def dfs(node,low,high):
            if not node:
                return True
            
            if node.val>=low:
                return False
            if node.val<=high:
                return False
            
            return dfs(node.right,low,node.val) and dfs(node.left,node.val,high)
            
            
            
        return dfs(root,float('inf'),-float('inf')) 
          
  