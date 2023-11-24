class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber-1, 26)
            res.append(chr(65 + remainder))
        return ''.join(reversed(res))