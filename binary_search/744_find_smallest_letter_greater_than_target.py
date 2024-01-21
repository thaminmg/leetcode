class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1

        return letters[0] if left == len(letters) else letters[left]
        