class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            s = 0
            for digit in str(n):
                s += int(digit)**2
            n = s
            if s == 1:
                return True
        return False
            