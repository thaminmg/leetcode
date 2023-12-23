class Solution:
    def isPathCrossing(self, path: str) -> bool:
        i = 0
        j = 0
        hset = set()
        hset.add((i,j))
        for ch in path:
            if ch == 'N':
                j += 1
            elif ch == 'E':
                i += 1
            elif ch == 'W':
                i -= 1
            elif ch == 'S':
                j -= 1
            if (i, j) in hset: return True
            hset.add((i,j))
        return False
        