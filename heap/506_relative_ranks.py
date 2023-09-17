class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxHeap = []
        for idx, val in enumerate(score):
            heapq.heappush(maxHeap, (-val, idx))

        place = 1
        res = [''] * len(score)
        while maxHeap:
            pos = heapq.heappop(maxHeap)[1]
            if place > 3:
                rank = str(place)
            elif place == 1:
                rank = 'Gold Medal'
            elif place == 2:
                rank = 'Silver Medal'
            elif place == 3:
                rank = 'Bronze Medal'
            
            res[pos] = rank
            place += 1
            
        return res

        