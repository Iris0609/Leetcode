##medium
##binary tree
## 94.26% ,56ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right

            
#         self.res=None
#         self.k=k
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             self.k-=1
#             if self.k==0:
#                 self.res=node.val
#             dfs(node.right)
            
#         dfs(root)
#         return self.res