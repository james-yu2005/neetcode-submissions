class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two choices at every step (either open or close paren)
        ans = []
        def backtrack(i,curr,o,c):
            if len(curr) == 2*n:
                if o == c:
                    ans.append(curr)
                return
            if c > o:
                return
            backtrack(i+1,curr+'(',o+1,c)
            backtrack(i+1,curr+')',o,c+1)

        backtrack(0,'',0,0)
        return ans
        