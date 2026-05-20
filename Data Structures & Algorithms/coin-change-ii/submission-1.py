class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # At each step, you can make two choices: choose this coin or move on to the next
        dp = [0 for i in range(amount+1)]
        print(dp)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]
        [1,1,2,4,7]