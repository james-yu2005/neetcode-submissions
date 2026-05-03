from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1,c2 = dict(),dict()
        for i in range(len(s1)):
            c1[s1[i]] = c1.get(s1[i],0) + 1
            c2[s2[i]] = c2.get(s2[i],0) + 1
        print(c1)
        print(c2)
        i = 0
        for j in range(len(s1),len(s2)):
            if c1 == c2:
                return True
            if c2[s2[i]] == 1:
                c2.pop(s2[i])
            else:
                c2[s2[i]] -= 1
    
            c2[s2[j]] = c2.get(s2[j],0) + 1
            i += 1
        return c1 == c2
