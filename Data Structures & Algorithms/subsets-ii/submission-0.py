class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        
        def get_sub(i,curr):
            if i == n:
                ans.append(curr.copy())
                return
            get_sub(i+1, curr + [nums[i]])
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
                print(i)
            get_sub(i+1, curr)
        get_sub(0,[])
        # if u decide to reject a 1, then you can never accept it again
        return ans