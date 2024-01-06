class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hset = defaultdict(str)
        lst = s.split(' ')
        if len(pattern) != len(lst): return False
        for i in range(len(pattern)):
            if pattern[i] not in hset and lst[i] not in hset.values(): 
                hset[pattern[i]] = lst[i]
            if hset[pattern[i]] != lst[i]:
                return False
        return True

         