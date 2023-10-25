from itertools import permutations

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')
            
            if right < left:
                dfs(left, right + 1, s + ')')

        res = []

        dfs(0, 0, '')
        return res

        # def check(lst):
        #     stack = []
        #     for l in lst:
        #         if l == ')':
        #             if not stack:
        #                 return False
        #             else:
        #                 stack.pop()
        #         else:
        #             stack.append(l)
        #     return True
        # perms = permutations(['('] * n + [')'] * n)
        # res = []
        # hset = set(perms)
        # for p in list(hset):
        #     if  check(p):
        #         res.append(''.join(p))
        # return res
       
        