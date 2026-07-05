class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # brute force method is just to check every possible balloon pop combination
        # impossible to compute all subproblems (if there are 5 balloons, and we choose to)
        # pop the second one, it's impossible because each depends on the other 
        # instead, let's think of which balloon which choose to pop last!
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if l > r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            max_coins = 0
            for i in range(l,r+1):
                # if this is the one we choose to pop last, then everything in the range
                # would be gone by the time we get to it
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l,i-1) + dfs(i+1,r)
                max_coins = max(coins,max_coins)
                dp[(l,r)] = max_coins
            return max_coins
        return dfs(1,len(nums)-2)