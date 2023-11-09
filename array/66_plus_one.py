class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        digits[0] += 1

        for i in range(len(digits) - 1):
            if digits[i] > 9:
                digits[i+1] += 1
                digits[i] = 0 

        if digits[-1] > 9:
            digits[-1] = 0
            digits.append(1)

        digits.reverse()

        return digits
        