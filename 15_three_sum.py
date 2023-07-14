class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for idx, a in enumerate(nums):
            if idx > 0 and a == nums[idx - 1]:
                continue
            
            l = idx + 1
            r = len(nums) - 1
            while r > l:
                if a + nums[l] + nums[r] == 0 :
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and r > l:
                        l += 1
                elif a + nums[l] + nums[r] > 0 :
                    r -= 1
                else:
                    l += 1
        return result


# nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0,0]
print(Solution().threeSum(nums))