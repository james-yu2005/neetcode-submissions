class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # at every letter index, we can choose to add this
        # to previous palindrome or start a new one
        n = len(s)
        ans = []
        def backtrack(i,curr):
            if i == n:
                ans.append(curr.copy())
                return
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    backtrack(j+1,curr)
                    curr.pop()
        backtrack(0,[])
        return ans
        
