class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                seen.remove(nums[i])
        backtrack([])
        return ans
