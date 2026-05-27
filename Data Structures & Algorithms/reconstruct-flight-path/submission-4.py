class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = { src: [] for src,_ in tickets}
        for src,dst in tickets:
            adj[src].append(dst)

        ans = ["JFK"]
        def dfs(src):
            if len(ans) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            for i,dest in enumerate(list(adj[src])):
                adj[src].pop(i)
                ans.append(dest)
                if dfs(dest):
                    return True
                adj[src].insert(i,dest)
                ans.pop()
        dfs("JFK")
        return ans
                
        
            
