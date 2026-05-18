class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num,0) + 1
        
        for key,value in num_count.items():
            heapq.heappush(h,(value,key))
            if len(h) > k:
                heapq.heappop(h)
        
        return [k for v,k in h]