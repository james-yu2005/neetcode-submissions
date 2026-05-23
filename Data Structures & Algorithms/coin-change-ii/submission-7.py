class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # try depth first search aka top down approach
        # you can choose to add the coin, or move on to next coin
        # memo[i][a] stores number of ways to form amount a using coins i and forward
        memo = [[-1] * (amount+1) for _ in range(len(coins))]
        def dfs(i,a):
            if i == len(coins) or a > amount:
                return 0
            if a == amount:
                return 1
            if memo[i][a] != -1:
                return memo[i][a]

            res = dfs(i+1,a)
            res += dfs(i,coins[i]+a)
            
            memo[i][a] = res
            return res

        return dfs(0,0)
        
            
        #           a=0 -> a=4
        # coin[0] 1 [1,0,0,0,0
        # coin[1] 2  1,0,0,0,0
        # coin[2] 3  1,0,0,0,0
        #            1,0,0,0,0]




