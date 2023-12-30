class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hset = defaultdict(int)
        for word in words:
            for ch in word:
                hset[ch] += 1

        n = len(words)
        for val in hset.values():
            if val % n != 0:
                return False
        return True
        