class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def back(curr):
            if len(curr) == n:
                ans.append(curr.copy())
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    back(curr)
                    curr.pop()
        back([])
        return ans
            
