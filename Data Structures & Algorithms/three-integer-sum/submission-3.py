class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        seen = set()
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    triplet = (nums[i], nums[l], nums[r])
                    if triplet not in seen:
                        ans.append([nums[i], nums[l], nums[r]])
                        seen.add(triplet)
                    l += 1
                    r -= 1
        return ans

