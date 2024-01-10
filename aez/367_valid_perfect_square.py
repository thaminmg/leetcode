class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        squareRoot = int(num ** 0.5)
        return squareRoot * squareRoot == num
        