class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap,-num)
        
        while len(heap) > 1:
            r1 = -heapq.heappop(heap)
            r2 = -heapq.heappop(heap)
            if r1 == r2:
                continue
            elif r1 > r2:
                heapq.heappush(heap,r2-r1)
            else:
                heapq.heappush(heap,r1-r2)
        
        return -heap[0] if len(heap) == 1 else 0

            

            
