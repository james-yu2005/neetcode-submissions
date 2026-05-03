class Solution:
    def encode(self, strs: List[str]) -> str:
        # encode it by first showing the number then counting that number of strings
        ans = ""
        for wrd in strs:
            ans += (str(len(wrd)) + ',' + wrd)
        return ans

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ',':
                j += 1
            num = int(s[i:j])
            wrd = s[j+1:j+1+num]
            ans.append(wrd)
            i = j + 1 + num
        return ans
        # 5,hello5,world
