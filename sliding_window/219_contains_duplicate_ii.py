class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}

        for idx, num in enumerate(nums):
            if num in hset:
                if idx - hset[num] <= k:
                    return True
            hset[num] = idx
        return False
        