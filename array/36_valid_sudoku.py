class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(nums):
            while '.' in nums: nums.remove('.')
            return len(set(nums)) == len(nums)

        for i in range(9):
            row = board[i]
            col = []
            for j in range(9):
                col.append(board[j][i])
            
            sqr = []
            for x in range(3*(i%3),3*(i%3)+3):
                for y in range(3*(i//3), 3*(i//3)+3):
                    sqr.append(board[x][y])

            if not (isValid(row.copy()) and isValid(col.copy()) and isValid(sqr.copy())):
                return False
        return True

        