class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq_count = [[] for i in range(len(nums)+1)]
        int_map = {}
        for num in nums:
            int_map[num] = int_map.get(num,0) + 1

        for key,value in int_map.items():
            freq_count[value].append(key)
        
        for i in range(len(freq_count)-1,-1,-1):
            if freq_count[i] and k > 0:
                ans.extend(freq_count[i])
                k -= len(freq_count[i])
        
        return ans