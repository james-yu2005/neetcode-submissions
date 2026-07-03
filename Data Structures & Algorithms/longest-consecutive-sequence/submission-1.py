class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        # loop through, if the n-1 exists then dont start
        max_ans = 0
        for num in nums:
            temp = num
            ans = 0
            if (temp-1) not in nums:
                while temp in nums:
                    temp += 1
                    ans += 1
            max_ans = max(max_ans,ans)
        return max_ans