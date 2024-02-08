class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hset = {}
        for num in nums:
            if num not in hset:
                hset[num] = 1
            else:
                hset[num] += 1
        result = []
        limit = sorted(hset.values())
        limit.reverse()
       
        for key, value in hset.items():
            
            if value in limit[:k]:
                result.append(key)
        return result

nums = [-1, -1]
# nums = [1,1,1,2,2,3]
k = 1
print(Solution().topKFrequent(nums, k))