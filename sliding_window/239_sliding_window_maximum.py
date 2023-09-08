import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []

        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output


nums = [1,3,-1,-3,5,3,6,7] 
k = 3
print(Solution().maxSlidingWindow(nums, k))