class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxx = 0
        # n = len(height)
        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         area = min(height[i], height[j]) * (j - i)
        #         maxx = area if area > maxx else maxx
        # return maxx
        maxx = 0
        l, r = 0, len(height) - 1

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            maxx = max(curr, maxx)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxx
        