class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        max_window = -1
        curr_sum = 0
        l = 0
        target = sum(nums) - x
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l <= r and curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            if curr_sum == target:
                max_window = max(max_window, r - l + 1)
        return -1 if max_window == -1 else len(nums) - max_window
        # not work for all cases
        # temp = x
        # count = 0
        # while x > 0 and nums:
        #     first = nums[0]
        #     last = nums[-1]
        #     if first >= last:
        #         if x >= first:
        #             x -= first
        #             nums.pop(0)
        #             count += 1
        #         elif x >= last:
        #             x -= last
        #             nums.pop()
        #             count += 1
        #         else:
        #             print(count)
        #             return -1                    
        #     else:
        #         if x >= last:
        #             x -= last
        #             nums.pop()
        #             count += 1
        #         elif x >= first:
        #             x -= first
        #             nums.pop(0)
        #             count += 1
        #         else:
        #             print(count)

        #             return -1

        # if x == 0:
        #     return count
        # else:
        #     print(count)
        #     return -1