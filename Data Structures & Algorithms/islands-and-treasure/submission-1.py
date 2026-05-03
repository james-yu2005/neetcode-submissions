class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        rows,cols = len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            r,c = q.popleft()
            for d in direc:
                nr,nc = d[0]+r,d[1]+c
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))
        
                                


