class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1+n2 != len(s3):
            return False

        dp = [[False for _ in range(n1+1)] for _ in range(n2+1)]
        dp[0][0] = True
        # main loop to determine bool
        for i in range(n2+1):
            for j in range(n1+1):
                if j != 0:
                    if dp[i][j-1] and s3[i+j-1] == s1[j-1]:
                        dp[i][j] = True
                if i != 0:
                    if dp[i-1][j] and s3[i+j-1] == s2[i-1]:
                        dp[i][j] = True
        print(dp)
        return dp[n2][n1]
        
        

        