class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        ans = 0
        minHeap = []

        # Calculate distances from each node to another
        adj_dist = {(x,y): [] for x,y in points}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                # the value is in format [distance,x_dest,y_dest]
                adj_dist[(x1,y1)].append([dist,x2,y2])
                adj_dist[(x2,y2)].append([dist,x1,y1])

        # Use prim's algorithm; iterate through each and find frontier
        start = tuple(points[0])
        seen.add(start)
        while len(seen) < len(points):
            for d,x,y in adj_dist[start]:
                if (x,y) in seen:
                    continue
                heapq.heappush(minHeap,(d,x,y))
            min_dist,targ_x,targ_y = heapq.heappop(minHeap)
            while (targ_x,targ_y) in seen:
                min_dist,targ_x,targ_y = heapq.heappop(minHeap)
            ans += min_dist
            seen.add((targ_x,targ_y))
            start = (targ_x,targ_y)
        return ans

