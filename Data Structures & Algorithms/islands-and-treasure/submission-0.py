class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        treasures = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    treasures.append([i,j,0])
        q = deque(treasures)

        while q:
            t = q.popleft()
            if t[0] < 0 or t[0] > rows-1 or t[1] < 0 or t[1] > cols-1:
                continue
            if grid[t[0]][t[1]] == 2147483647:
                grid[t[0]][t[1]] = t[2]
            for d in directions:
                if t[0]+d[0] < 0 or t[0]+d[0] > rows-1 or t[1]+d[1] < 0 or t[1]+d[1] > cols-1:
                    continue
                if grid[t[0]+d[0]][t[1]+d[1]] == 2147483647:
                    q.append([t[0]+d[0],t[1]+d[1],t[2]+1])

        return None

