class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        j = 0
        for num in nums:
            arr[num] += 1
        [1,2,1]
        for i in range(len(nums)):
            while arr[j] == 0:
                j += 1
            nums[i] = j
            arr[j] -= 1
        
        return nums
