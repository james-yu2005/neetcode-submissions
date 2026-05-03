class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i < 2 or dp[i+1][j-1]:
                        dp[i][j] = True
        
        def backtrack(i,curr):
            if i == n:
                ans.append(curr.copy())
            for j in range(i,n):
                if dp[i][j]:
                    curr.append(s[i:j+1])
                    backtrack(j+1,curr)
                    curr.pop()
        backtrack(0,[])
        return ans
        

