class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        neighbors = {i: [] for i in range(n)}
        for s,e in edges:
            neighbors[s].append(e)
            neighbors[e].append(s)
        print(neighbors)
        def connections(node,seen):
            if node in seen:
                return
            seen.add(node)
            for neigh in neighbors[node]:
                connections(neigh,seen)
        seen = set()
        connections(0,seen)
        return len(seen) == n