class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try some middle number first or try max
        l,r = 1,max(piles)
        min_rate = float('inf')
        while l <= r:
            rate = (l+r)//2
            print(l,r)
            tot_hours = 0
            for pile in piles:
                hours = pile//rate
                hours = hours if pile % rate == 0 else hours + 1
                tot_hours += hours
            print(tot_hours)
            print(rate)
            if tot_hours < h:
                r = rate - 1
                min_rate = min(min_rate,rate)
            elif tot_hours > h:
                l = rate + 1
            else:
                r = rate - 1
                min_rate = min(min_rate,rate)

        return min_rate


