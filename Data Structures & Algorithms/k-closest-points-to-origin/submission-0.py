class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_to_loc = {}
        heap = []
        for i,(x,y) in enumerate(points):
            dist = float((x**2 + y**2)**(1/2))
            dist_to_loc[(-dist,i)] = [x,y]
            heapq.heappush(heap,(-dist,i))
            if len(heap) > k:
                heapq.heappop(heap)
            
        return [dist_to_loc[x] for x in heap]

        
        

        