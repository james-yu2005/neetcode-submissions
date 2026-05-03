import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+':
                n1 = st.pop()
                n2 = st.pop()
                ans = int(n1) + int(n2)
                st.append(ans)
            elif t == '-':
                n1 = st.pop()
                n2 = st.pop()
                ans = int(n2) - int(n1)
                st.append(ans)
            elif t == '*':
                n1 = st.pop()
                n2 = st.pop()
                ans = int(n1) * int(n2)
                st.append(ans)
            elif t == '/':
                n1 = st.pop()
                n2 = st.pop()
                ans = int(int(n2)/int(n1))
                st.append(ans)
            else:
                st.append(t)
        return int(st[-1])
