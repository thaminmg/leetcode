class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        minHeap = []
        for i in range(len(mat)):
            count = mat[i].count(1)
            heapq.heappush(minHeap, (count, i))
        return [heapq.heappop(minHeap)[1] for _ in range(k)]
        