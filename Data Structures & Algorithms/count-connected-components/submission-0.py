from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        seen = set()
        cycles = 0
        # DFS
        def find_comp(node):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                find_comp(nei)

        for i in range(n):
            if i in seen:
                continue
            find_comp(i)
            cycles += 1
        return cycles


        