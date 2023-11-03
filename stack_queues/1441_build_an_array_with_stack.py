class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        stack = []

        for i in range(1, n+1):
            if i in target:
                res.append('Push')
                stack.append(i)
            else:
                res.append('Push')
                res.append('Pop')
            if stack == target:
                return res
        return res


        