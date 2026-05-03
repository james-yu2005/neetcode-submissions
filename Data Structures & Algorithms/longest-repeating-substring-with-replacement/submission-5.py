class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # condition, while window - most frequent > k
        # other key condition, u ONLY care about max frequency
        i = 0
        max_freq = 0
        ans = 0
        curr_count = dict()
        for j,c in enumerate(s):
            curr_count[c] = curr_count.get(c,0) + 1
            max_freq = max(max_freq,curr_count[c])
            while j-i+1 - max_freq > k:
                curr_count[s[i]] -= 1
                i += 1
            ans = max(ans,j-i+1)
            print(ans,i)
        return ans