
## medium
##72ms, 15.04%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        leftbound=[]
        childbound=[]
        rightbound=[]
        res=[]
        if not root:
            return []
        res.append(root.val)
        
        def leftdfs(node):
            if not node:
                return
            leftbound.append(node.val)
            if node.left:
                leftdfs(node.left)
            else:
                leftdfs(node.right)
            
        def childdfs(node):
            if not node:
                return
            if node.left==None and node.right==None:
                childbound.append(node.val)
                return
            else:
                childdfs(node.left)
                childdfs(node.right)
                
        def rightdfs(node):
            if not node:
                return
            if node.right:
                rightdfs(node.right)
            else:
                rightdfs(node.left)
            rightbound.append(node.val)
            
        leftdfs(root.left)

        childdfs(root)

        rightdfs(root.right)

        res+=leftbound
        if leftbound==[] and rightbound==[]:
            res+=[]    
        elif leftbound==[] and rightbound:
            res+=childbound
        else:
            res+=childbound[1:]
        
        if not childbound:
            res+=rightbound
        else:
            res+=rightbound[1:]
        
        # res = list(set(bound))
        # res.sort(key=bound.index)
        
        return res
                
                