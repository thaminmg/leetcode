class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

        # hset = set()
        # temp = nums.copy()
        # for num in temp:
        #     if num in hset:
        #         nums.remove(num)
        #     else:
        #         hset.add(num)
        # return len(nums)
        