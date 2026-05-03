class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        ans = 0         
        visit = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for neigh in adj[node]:
                dfs(neigh)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                ans += 1
        return ans
        

        {0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}