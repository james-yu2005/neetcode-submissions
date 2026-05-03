class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_strs = defaultdict(list)
        for s in strs:
            freq = [0 for _ in range(26)]
            for c in s:
                freq[ord(c)-ord('a')] += 1
            freq_to_strs[tuple(freq)].append(s)
        print(freq_to_strs) 
        return list(freq_to_strs.values())