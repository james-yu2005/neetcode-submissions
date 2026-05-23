class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # use top down approach (DFS)

        def dfs(s,i):
            if i == len(nums):
                if s == target:
                    return 1
                else:
                    return 0

            res = dfs(s+nums[i],i+1) + dfs(s-nums[i],i+1)
            return res
        
        return dfs(0,0)
