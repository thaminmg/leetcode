class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        curr = 0
        curr2 = 0
        if not nums1:
            p1 = -1
        if not nums2:
            p2 = -1
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        idx1 = 0
        idx2 = 0
        if n % 2 == 0:
            idx2 = n // 2
            idx1 = idx2 - 1
        else:
            idx1 = n // 2
        if p1 == -1 or p2 == -1:
            if not p1:
                if not idx2:
                    return nums1[idx1]
                else:
                    return (nums1[idx1] + nums1[idx2] ) /2
            if not p2:
                if not idx2:
                    return nums2[idx1]
                else:
                    return (nums2[idx1] + nums2[idx2] ) /2
        while p1 < n1 or p2 < n2:
            n -= 1
            if p1 >= 0 and nums1[p1] <= nums2[p2]:
                curr = nums1[p1]
                p1 = p1 + 1 if p1 < n1 - 1 else -1
            elif p1 == -1:
                curr = nums2[p2]
                p2 = p2 + 1 if p2 < n2 - 1 else -1
            elif p2 >= 0:
                curr = nums2[p2]
                p2 = p2 + 1 if p2 < n2 - 1 else -1
            elif p2 == -1: 
                curr = nums1[p1]
                p1 = p1 + 1 if p1 < n1 - 1 else -1

            if idx2 == 0 and idx1 == n:
                return curr
            if idx2 == n and idx1 == n - 1:
                if p1 >= 0 and nums1[p1] <= nums2[p2]:
                    curr2 = nums1[p1]
                elif p1 == -1 and nums1[p1] <= nums2[p2]:
                    curr2 = nums2[p2]
                elif p2 >= 0: 
                    curr2 = nums2[p2]
                elif p2 == -1: 
                    curr2 = nums1[p1]
                return (curr + curr2) / 2
            
            

        return 0
             
        