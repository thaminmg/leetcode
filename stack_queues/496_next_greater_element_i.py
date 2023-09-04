class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        result = [-1] * len(nums1)

        for index, val in enumerate(nums1):
            for j in nums2:
                if j == val:
                    stack.append(j)
                else:
                    if stack and j > stack[-1]:
                        result[index] = j
                        break
            stack.clear()
                    
        return result
        