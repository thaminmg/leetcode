class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        
        left, right = 2, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            
            res = mid * mid
            if res == num:
                return True
            elif res > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        