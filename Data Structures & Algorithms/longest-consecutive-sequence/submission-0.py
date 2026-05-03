class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_cons = 0
        for num in nums:
            curr = num
            cons = 0
            if (curr-1) not in nums:
                while curr in nums:
                    curr += 1
                    cons += 1
            max_cons = max(max_cons,cons)
        return max_cons
