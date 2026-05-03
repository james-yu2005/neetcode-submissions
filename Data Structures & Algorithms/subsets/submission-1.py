class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        curr = []
        def find_sub(i):
            if i == n:
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            find_sub(i+1)
            curr.pop()
            find_sub(i+1)
        find_sub(0)
        return ans
            