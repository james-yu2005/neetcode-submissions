class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        ans = [0 for _ in range(n)]
        for i,t in enumerate(temperatures):
            while st and t > st[-1][1]:
                idx,_ = st.pop()
                ans[idx] = i-idx
            if not st or t <= st[-1][1]:
                st.append((i,t))
        return ans

