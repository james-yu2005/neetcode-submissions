class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices)==1:
            return 0
        n = len(prices)
        if n == 2:
            if prices[0] < prices[1]:
                return prices[1]-prices[0]
            else:
                return 0
        # 2 options a day, hold, cash or cool
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1,n):
            # to hold today, either held yesterday and continue, or just bought from resting phase
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])

            # to cash today, just cashed
            dp[i][1] = dp[i-1][0] + prices[i]

            # to be on cooldown, either just bought, or just continue cooldown max
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[n-1][1],dp[n-1][2])
        