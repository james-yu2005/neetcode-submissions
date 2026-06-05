class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # have to factor in length of path
        # djistra's algorithm basically appending to the queue, but in this case
        # we track number of paths and when that reaches k we stop
        adj = { i: [] for i in range(n)}
        for s,d,cost in flights:
            adj[s].append((d,cost))

        minHeap = [(0,src,-1)]

        while minHeap:
            cost,curr,stops = heapq.heappop(minHeap)
            if k >= stops and curr == dst:
                return cost
            if stops > k:
                continue
            for next_stop,cost_add in adj[curr]:
                heapq.heappush(minHeap,(cost_add + cost,next_stop,stops+1))

        return -1