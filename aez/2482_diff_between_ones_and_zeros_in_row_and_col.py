class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRowMap = defaultdict(int)
        onesColMap = defaultdict(int)
        zerosRowMap = defaultdict(int)
        zerosColMap = defaultdict(int)

        res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def onesRow(i):
            if i in onesRowMap: return onesRowMap[i]
            onesRowMap[i] = sum(grid[i])
            return onesRowMap[i]

        def onesCol(j):
            if j in onesColMap: return onesColMap[j]
            onesColMap[j] = sum(row[j] for row in grid)
            return onesColMap[j]

        def zerosRow(i):
            if i in zerosRowMap: return zerosRowMap[i]
            zerosRowMap[i] = grid[i].count(0)
            return zerosRowMap[i]


        def zerosCol(j):
            if j in zerosColMap: return zerosColMap[j]
            zerosColMap[j] = [row[j] for row in grid].count(0)
            return zerosColMap[j]

        def diff(i, j):
            return onesRow(i) + onesCol(j) - zerosRow(i) - zerosCol(j)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(i, j)
                res[i][j] = diff(i, j)

        return res