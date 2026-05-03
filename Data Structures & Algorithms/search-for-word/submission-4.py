class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols = len(board), len(board[0])

        def backtrack(i,r,c,seen):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r,c) in seen or board[r][c] != word[i]:
                return False
        
            seen.add((r,c))
            for dr,dc in direc:
                nr,nc = r+dr, c+dc
                if backtrack(i+1,nr,nc,seen):
                    return True
            seen.remove((r,c))
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(0,i,j,set()):
                        return True
        return False
        
            

