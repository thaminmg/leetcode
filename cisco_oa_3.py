
"""
matrix, represents the elements of the matrix of size N*M.
"""
def funcMatrix(matrix):
	# Write your code here
    r, c = len(matrix), len(matrix[0])
    for i in range(r):
        maxRow = max(matrix[i])
        for j in range(c):
            col = []
            for k in range(r):
                col.append(matrix[k][j])   
            if maxRow == min(col) :
                return matrix[i][j]    
    return -1

def main():
	#input for matrix
	matrix = []
	matrix_rows,matrix_cols  = map(int, input().split())
	for idx in range(matrix_rows):
		matrix.append(list(map(int, input().split())))
	
	
	result = funcMatrix(matrix)
	print(result)	

main()