class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        n = len(height)
        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])  
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        return water


        