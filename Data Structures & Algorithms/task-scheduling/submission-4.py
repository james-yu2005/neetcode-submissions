class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        q = deque()
        freq = [0] * 26
        # build frequency array and push to max heap
        for task in tasks:
            freq[ord(task)-ord('A')] += 1
        for i in range(25,-1,-1):
            if freq[i] != 0:
                heapq.heappush(heap,(-freq[i]))
        print(heap)

        # start tracking time using queue and max heap
        time = 0
        while heap or q:
            time += 1
            if heap:
                freq = heapq.heappop(heap)
                if freq + 1 != 0:
                    print(freq+1, time+n)
                    q.append((freq+1,time+n))
            if q and q[0][1] == time:
                freq,_ = q.popleft()
                heapq.heappush(heap,freq)
        return time
        


    


