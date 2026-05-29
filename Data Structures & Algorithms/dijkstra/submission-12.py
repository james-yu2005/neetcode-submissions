class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = { i: [] for i in range(n)}
        for strt,dest,weight in edges:
            adj[strt].append([weight,dest])
        print(adj)
        ans = { i: -1 for i in range(n)}
        minHeap = [(0,src)]
        while minHeap:
            node_w,node = heapq.heappop(minHeap)
            if ans[node] != -1:
                continue
            ans[node] = node_w
            for neigh_w,neigh in adj[node]:
                if ans[neigh] == -1:
                    heapq.heappush(minHeap,(neigh_w + node_w,neigh))
                    
        return ans