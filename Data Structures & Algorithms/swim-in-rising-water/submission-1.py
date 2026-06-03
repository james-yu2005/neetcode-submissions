class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = []
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ans = 0
        
        minHeap.append((grid[0][0],0,0))
        while minHeap:
            time,x,y = heapq.heappop(minHeap)
            visited.add((x,y))
            ans = max(time,ans)
            for dx,dy in directions:
                nx = x + dx
                ny = y + dy
                if (nx,ny) == (rows-1,cols-1):
                    return max(ans,grid[nx][ny])
                if (nx,ny) in visited or (nx < 0 or nx >= rows) or (ny < 0 or ny >= cols):
                    continue
                heapq.heappush(minHeap,(grid[nx][ny],nx,ny))
        return ans
        
