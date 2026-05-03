# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        for i,pair in enumerate(pairs):
            key_pair = pairs[i]
            j = i-1
            while j >= 0 and pairs[j].key > key_pair.key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = key_pair
            ans.append(pairs[:])
        return ans