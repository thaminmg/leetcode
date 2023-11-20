import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.og = list(nums)    

    def reset(self) -> List[int]:
        self.nums = self.og
        self.og = list(self.og)
        return self.nums   

    def shuffle(self) -> List[int]:
        aux = list(self.nums)

        for idx in range(len(self.nums)):
            remove_idx = random.randrange(len(aux))
            self.nums[idx] = aux.pop(remove_idx)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()