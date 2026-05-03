class Solution:

    def encode(self, strs: List[str]) -> str:
        # word, some break, then word number
        # 4#neet4#code4#love3#you
        s = ""
        for st in strs:
            s += str(len(st))
            s += '#'
            s += st
        print(s)
        
        return s
    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        strs = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs.append(s[i:j])
            i = j
        return strs
            

        
        return strs



        
