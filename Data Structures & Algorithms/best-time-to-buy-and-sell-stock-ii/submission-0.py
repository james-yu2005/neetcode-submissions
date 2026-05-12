class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(len(prices)+1)]for _ in range(2)]
        # row 1 is if buying and row 2 is seling

        for i in range(len(prices)-1,-1,-1):
            dp[0][i] = max(dp[0][i+1],-prices[i]+dp[1][i+1])
            dp[1][i] = max(dp[1][i+1],prices[i]+dp[0][i+1])
        
        return dp[0][0]