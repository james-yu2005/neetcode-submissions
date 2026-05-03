class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_h = []
        seen = set()
        # count all nodes
        ans = 0
        # build graph
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append([v,t])
        
        heapq.heappush(min_h, (0,k))
        while min_h:
            path,node = heapq.heappop(min_h)
            if node in seen:
                continue
            seen.add(node)
            ans = max(ans,path)
            
            if len(seen) == n:
                return ans

            for v,t in adj[node]:
                heapq.heappush(min_h,(path + t,v))
                
        return ans if len(seen) == n else -1