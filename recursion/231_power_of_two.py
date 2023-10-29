class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return bin(n).count('1') == 1 and n >= 0
        # if n == 0: 
        #     return False
        # else:
        #     return n & (n - 1) == 0

        def recursion(n):
            if n == 1:
                return True
            if n == 0 or n % 2 != 0:
                return False
            return recursion(n / 2)
        return recursion(n)