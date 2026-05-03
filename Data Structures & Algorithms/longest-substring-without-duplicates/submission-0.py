class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        seen = set()
        for j,c in enumerate(s):
            while c in seen:
                seen.remove(s[i])
                i += 1
            seen.add(c)
            ans = max(ans,j-i+1)
        return ans

            
