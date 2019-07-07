
##medium
##44ms, 96.45%
##hashtable

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isunitvalid(unit):
            l=[i for i in unit if i!='.']
            return len(set(l))==len(l)
            
        def isrowvalid(board):
            for row in board:
                if not isunitvalid(row):
                    return False
            return True
            
        def iscolvalid(board):
            for col in zip(*board):
                if not isunitvalid(col):
                    return False
            return True
            
        def issquarevalid(board):
            for r in (0,3,6):
                for c in (0,3,6):
                    square=[board[x][y] for x in range(r,r+3) for y in range(c,c+3)]
                    if not isunitvalid(square):
                        return False
            return True
                    
            
        return isrowvalid(board) and iscolvalid(board) and issquarevalid(board)