## medium
## 204ms, beats 90.38%
## graph, dfs, array
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False

        row = len(board)
        col=len(board[0])


        # check whether can find word, start at (r,c) position   
        def search(r,c,w):
            if not w:
                return True
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=w[0]:
                return False
            # first character is found, check the remaining part
            tmp=board[r][c]
            # avoid visit agian
            board[r][c]='*'
            # check 4 direction around (r,c)
            res=search(r-1,c,w[1:]) or search(r,c+1,w[1:]) or search(r+1,c,w[1:]) or search(r,c-1,w[1:]) 
            # backtracking
            
            board[r][c] = tmp
            return res
    
        
        for i in range(row):
            for j in range(col):
                if search(i,j,word[0:]):
                    return True

        return False
        
                   
        