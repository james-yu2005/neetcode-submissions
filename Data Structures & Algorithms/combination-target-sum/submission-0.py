class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        def dfs(i,curr,tar):
            if tar > target or i == len(nums):
                return
            if tar == target:
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i,curr,tar+nums[i])
            curr.pop()
            dfs(i+1,curr,tar)
        dfs(0,[],0)
        return ans


