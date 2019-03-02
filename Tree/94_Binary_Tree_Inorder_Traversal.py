##medium
## hashtable, stack, tree
## 32ms, beats 100%, memory use 6.4mb beats 90.11%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def traversal(root,res):
            if root:
                if root.left:
                    traversal(root.left,res)
                res.append(root.val)
                if root.right:
                    traversal(root.right,res)
 
        traversal(root,res)
        return res