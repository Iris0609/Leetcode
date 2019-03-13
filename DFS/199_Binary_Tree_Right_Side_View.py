
##medium
##tree dfs
## 44ms, beat 55.30%

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=[]
        d=[]
        
        def dfs(node,depth):
            if not node:
                return
            if depth not in d:
                res.append(node.val)
                d.append(depth)

            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        
        dfs(root,0)

        return res

##still dfs use stack
##bfs can use deque
##dfs 先进后出，bfs先进先出。append，leftpop
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=[]
        max_depth=-1
        stack=[(root,0)]
        
        while stack:
            node,depth=stack.pop()
            if node:
                if depth>max_depth:
                    res.append(node.val)
                    max_depth=max(max_depth,depth)
                    
                
                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
                
        return res

