class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        hmap = Counter(nums)
        res = []
        for key, val in hmap.items():
            if val > limit:
                res.append(key)
        return res
        