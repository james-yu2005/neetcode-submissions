class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        for i in range(abs(n)):
            if n < 0:
                ans *= 1/x
            else:
                ans *= x
        return ans