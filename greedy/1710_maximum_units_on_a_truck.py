class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        maxHeap = []
        for box in boxTypes:
            heapq.heappush(maxHeap, (-box[1], -box[0]))
        res = 0
        remaining = truckSize
        used = 0
        while maxHeap and used < truckSize:
            curr = heapq.heappop(maxHeap)
            if used + abs(curr[1]) <= truckSize:
                res += abs(curr[1]) * abs(curr[0])
                remaining -= abs(curr[1])
                used += abs(curr[1])
            else:
                diff = truckSize - used
                if abs(curr[1]) > diff:
                    res += diff * abs(curr[0])
                    remaining -= diff
                    used += diff
                else:
                    res += abs(curr[1]) * abs(curr[0])
                    remaining -= abs(curr[1])
                    used += abs(curr[1])
        return res

        