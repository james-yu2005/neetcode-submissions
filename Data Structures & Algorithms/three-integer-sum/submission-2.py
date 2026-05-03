class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            targ = -nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[j] + nums[k]
                if s > targ:
                    k -= 1
                elif s < targ:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                    j += 1
        return ans