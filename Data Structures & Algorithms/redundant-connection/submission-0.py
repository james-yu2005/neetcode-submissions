class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu,pv = pv,pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    def find(self,node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        print(dsu.parent)
        for u,v in edges:
            if not dsu.union(u-1,v-1):
                return [u,v]
        