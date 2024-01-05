class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            temp = 0
            while n > 0:
                n, digit = divmod(n, 10)
                temp += digit ** 2
            return temp

        hset = set()
        while n != 1 and n not in hset:
            hset.add(n)
            n = helper(n)
        
        return n == 1
        