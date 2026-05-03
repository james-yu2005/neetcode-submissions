class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtrack(op,cl):
            if op == cl and len(stack) == n*2:
                ans.append("".join(stack))
                return

            if op < n:
                stack.append('(')
                backtrack(op+1,cl)
                stack.pop()
            if cl < op:
                stack.append(')')
                backtrack(op,cl+1)
                stack.pop()
        
        backtrack(0,0)
        return ans