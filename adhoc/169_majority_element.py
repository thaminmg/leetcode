class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums) >> 1
        counter = Counter(nums)

        for c in counter:
            if counter[c] > times:
                return c
        
        