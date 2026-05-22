class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # make a m * n array where m is len(coins) and n is amount+1
        # to make sure its unique we are building an array like this where in the same row an amount can only be summed by the coin values beneath it
        # Define dp array and set first row to all 1 (amount = 0 is always possible)
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        # first row
        for j in range(coins[0],amount+1):
            dp[0][j] += dp[0][j-coins[0]]

        # rest of rows
        for i in range(1,n):
            coin = coins[i]
            for j in range(amount+1):
                if j < coin:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-coin] + dp[i-1][j]  
        return dp[n-1][amount]
        #           a=0 -> a=4
        # coin[0] 1 [1,0,0,0,0
        # coin[1] 2  1,0,1,0,0
        # coin[2] 3  1,0,0,1,0]




