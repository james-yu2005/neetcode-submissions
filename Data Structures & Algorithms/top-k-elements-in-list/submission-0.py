class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums)+1)]
        {1:1, 2:2, 3:3}
        [[],[1],[2],[3],[],[],[]]
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num,cnt in count.items():
            freq[cnt].append(num)
        
        for i in range(len(nums),-1,-1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        return []