class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def back(i,curr):
            if i == len(digits):
                ans.append(curr)
                return
            for let in digit_map[digits[i]]:
                curr += let
                back(i+1,curr)
                curr = curr[:-1]
        back(0,"")
        return ans
       