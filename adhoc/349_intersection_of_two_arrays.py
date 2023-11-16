class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        res = []
        for i in range(len(nums2)):
            if nums2[i] in nums1 and nums2[i] not in res:
                res.append(nums2[i])
        return res
        