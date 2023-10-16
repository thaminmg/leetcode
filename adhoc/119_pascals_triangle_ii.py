class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]

        res = [1, 1]
        for i in range(2, rowIndex + 1):
            temp = []
            for j in range(len(res) - 1):
                temp.append(res[j] + res[j + 1])
            res = [1] + temp + [1]
        return res