class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0

        def isSpecialCol(idx):
            return sum(row[idx] for row in mat)

        for row in mat:
            if sum(row) == 1:
                colIdx = row.index(1)
                res += isSpecialCol(colIdx) == 1
        return res
        