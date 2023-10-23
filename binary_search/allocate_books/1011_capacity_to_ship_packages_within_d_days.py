class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def allocate(weights, mid):
            partition, total = 1, 0

            for w in weights:
                if total + w > mid:
                    total = 0
                    partition += 1
                total += w
            
            return partition

        left, right = max(weights), sum(weights)
        res = right


        while left <= right:
            mid = (left + right) // 2

            if allocate(weights, mid) <= days:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
        