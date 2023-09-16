class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones) 
        while len(stones) > 1:
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y-x))
        return - stones[0] if len(stones) > 0 else 0 

        # self.maxHeap, self.n = heapq._heapify_max(stones), len(stones)
        # counter = 0
        # while counter > 1:
        #     y = heapq._heappop_max(self.maxHeap)
        #     x = heapq._heappop_max(self.maxHeap)
        #     if (x != y):
        #         heapq._heappush_max(self.maxHeap, y - x)
        #     counter = len(self.maxHeap)
        # return self.maxHeap


        