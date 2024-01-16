class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        hset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for ch in s:
            if ch in hset:
                res.append(ch.lower())
            else:
                res.append(ch)

        return ''.join(res)
        