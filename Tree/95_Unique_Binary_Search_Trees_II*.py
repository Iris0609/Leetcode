# Medium
# 60 ms, beats 85.54%
# 14mb, beats 0.9%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def dfs(start,end):
            if start>end:
                return [None]
            res=[]
            for ind in range(start,end+1):
                left=dfs(start,ind-1)
                right=dfs(ind+1,end)
                for l in left:
                    for r in right:
                        tmp=TreeNode(ind)
                        tmp.left=l
                        tmp.right=r
                        res.append(tmp)
            return res
        
        if n==0:
            return []
        return dfs(1,n)

    