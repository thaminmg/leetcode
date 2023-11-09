class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        if n2 > n1:
            nums1, nums2 = nums2, nums1
        
        res = []
        for n in nums2:
            if n in nums1:
                nums1.remove(n)
                res.append(n)
        return res
        