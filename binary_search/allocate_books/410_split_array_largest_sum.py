class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = right
        def allocate(nums, limit):
            count, total = 1, 0
            for num in nums:
                if total + num > limit:
                    total = 0
                    count += 1
                total += num
            return count
        while left <= right:
            mid = (left + right) // 2
            if allocate(nums, mid) <= k:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

        # left, right = 0, sum(nums)
        # res = right

        # def check(nums, mid , k):
        #     no = 1
        #     total = 0
        #     for num in nums:
        #         if total <= mid:
        #             total += num
        #             if total > mid:
        #                 if num > mid:
        #                     return False                    
        #                 no += 1
        #                 total = num
            
        #     if no <= k:
        #         return True
        #     return False

        # while left <= right:
        #     mid = (left + right) // 2

        #     if check(nums, mid, k):
        #         res = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return res

        