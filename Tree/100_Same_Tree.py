##easy
##dfs,tree
##32ms,beats 100%
##12.7mb, beats 100%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        def dfs(p1,q1):
            if p1==None or q1==None:
                if p1==None and q1==None:
                    return True
                else:
                    return False
                
            if p1.val==q1.val:
                return dfs(p1.left,q1.left) and dfs(p1.right,q1.right)
            else:
                return False
            # return True
        return dfs(p,q)
        