class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s is the string we analyze and t is the one we are building 
        dp = {}

        # i is current position in s, and j is current position in t
        def dfs(i,j):
            # base case
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            paths = dfs(i+1,j)
            if s[i] == t[j]:
                paths += dfs(i+1,j+1)
            dp[(i,j)] = paths
            return paths
        return dfs(0,0)
            
            



