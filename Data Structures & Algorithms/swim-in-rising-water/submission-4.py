class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = []
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        minHeap.append((grid[0][0],0,0))
        while minHeap:
            time,x,y = heapq.heappop(minHeap)
            if x == rows-1 and y == cols-1:
                return time
            for dx,dy in directions:
                nx = x + dx
                ny = y + dy
                if (nx,ny) in visited or (nx < 0 or nx >= rows) or (ny < 0 or ny >= cols):
                    continue
                visited.add((nx,ny))
                heapq.heappush(minHeap,(max(grid[nx][ny],time),nx,ny))
    
        
