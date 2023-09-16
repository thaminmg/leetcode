class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heapq.heapify(result)
        for idx, pt in enumerate(points):
            distance = pt[0] * pt[0] + pt[1] * pt[1]
            heapq.heappush(result, (-distance, pt))
            if len(result) > k:
                heapq.heappop(result)
        return [pt[1] for pt in result]
        

        