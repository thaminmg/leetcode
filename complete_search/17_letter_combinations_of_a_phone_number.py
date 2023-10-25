class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hset = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def dfs(s, digits):
            if not digits:
                res.append(s)
                return
            for digit in hset[digits[0]]:
                dfs(s + digit, digits[1:])

        if digits:
            dfs('', digits)

        return res
        