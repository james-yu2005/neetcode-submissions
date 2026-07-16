class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            mid = (l+r)//2
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] <= nums[mid]:
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid
        return nums[l]


                    


                

            