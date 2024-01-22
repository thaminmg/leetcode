class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = []
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        
        while p1 < n1 and p2 < n2:
            left = nums1[p1]
            right = nums2[p2]
            
            if left == right:
                res.append(left)
                while p1 < n1 and left == nums1[p1]: 
                    p1 += 1
                while p2 < n2 and right == nums2[p2]: 
                    p2 += 1
                continue
            
            if left > right:
                while p2 < n2 and right == nums2[p2]: 
                    p2 += 1
            else:
                while p1 < n1 and  left == nums1[p1]: 
                    p1 += 1
        return res
                
        
        
            
        