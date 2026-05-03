class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = ""
        for i in range(len(strs)):
            s += strs[i]
            s += '-'

        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        curr_word = ""
        for char in s:
            if char == '-':
                strs.append(curr_word)
                curr_word = ""
            else:
                curr_word += char
        return strs

