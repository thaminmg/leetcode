class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1,1])
            else:
                temp = [1]
                for j in range(i - 1):
                    temp.append(triangle[i-1][j] + triangle[i-1][j+1])
                temp.append(1)
                triangle.append(temp)
        return triangle
        