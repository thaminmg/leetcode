class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            binary = str(bin(i))
            result.append(binary.count('1'))
        return result