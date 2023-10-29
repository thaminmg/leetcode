class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else math.log(n, 4).is_integer()
        
        