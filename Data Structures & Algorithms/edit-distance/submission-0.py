class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n1+1) for _ in range(n2+1)]
        # setting up first col and row because making word1 and word2
        # from nothing takes one more step each time
        for i in range(n1+1):
            dp[0][i] = i
        for i in range(n2+1):
            dp[i][0] = i
        
        # loop to build
        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # if its diff, u can replace, remove, or insert
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[n2][n1]

