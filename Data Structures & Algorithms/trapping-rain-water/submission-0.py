class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i,h in enumerate(height):
            left_max = self.left_max(i,height)
            right_max = self.right_max(i,height)
            trap = min(left_max, right_max) - height[i]
            ans += trap

        return ans

    def left_max(self, i: int, height: List[int]) -> int:
        left_max = 0
        for k in range(i,-1,-1):
            left_max = max(left_max,height[k])
            
        return left_max
            
    def right_max(self, i: int, height: List[int]) -> int:
        right_max = 0
        for k in range(i,len(height)):
            right_max = max(right_max,height[k])
        
        return right_max