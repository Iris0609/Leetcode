##medium
##44ms,60.34%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root:
            return res
        level=[]
        dq=deque()
        dq.append(root)
        cnt=1
        childcnt=0
        
        while dq:
            if cnt==0:
                res.append(level)
                level=[]
                cnt=childcnt
                childcnt=0
            node=dq.popleft()
            level.append(node.val)
            if node.left: 
                dq.append(node.left)
                childcnt+=1
            if node.right: 
                dq.append(node.right)
                childcnt+=1
            cnt-=1
        res.append(level)
            
        return res
            
        