class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0
        # just check every letter
        for _ in range(len(strs[0])):
            curr_let = strs[0][i]
            for wrd in strs:
                if i+1 > len(wrd) or wrd[i] != curr_let:
                    return ans
            ans += curr_let
            i += 1

        return ans
            