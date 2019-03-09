##hard
##112ms,85.09%
##13mb, beats 100%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        self.fir=None
        self.pre=TreeNode(-float('inf'))
        self.sec=None
        
        
        def lnr(node):
            if not node:
                return
            lnr(node.left)
            
            if self.fir==None and self.pre.val>=node.val:
                self.fir=self.pre
            if self.fir!=None and self.pre.val>=node.val:
                self.sec=node
                
            self.pre=node         
            
            lnr(node.right)
            
        
        
        lnr(root)
        self.fir.val,self.sec.val=self.sec.val,self.fir.val
    
