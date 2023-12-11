class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        limit = (n * 0.25)

        counter = Counter(arr)
        for letter, count in counter.items():
            if count > limit: return letter
        
        