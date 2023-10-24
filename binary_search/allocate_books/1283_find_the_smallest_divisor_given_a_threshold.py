class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        res = right

        def allocate(nums, mid):
            total = 0
            for num in nums:
                total += ceil(num / mid)
            return total

        while left <= right:
            mid = (left + right) // 2

            if allocate(nums, mid) <= threshold:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res 

        