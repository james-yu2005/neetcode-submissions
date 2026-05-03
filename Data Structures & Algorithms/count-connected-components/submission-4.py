from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        seen = [False for _ in range(n)]
        cycles = 0
        # DFS
        def find_comp(node):
            for nei in adj[node]:
                if not seen[nei]:
                    seen[nei] = True
                    find_comp(nei)

        for i in range(n):
            if not seen[i]:
                seen[i] = True
                find_comp(i)
                cycles += 1
        return cycles


        