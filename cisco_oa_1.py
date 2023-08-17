def funcRotate(inputMat: list[list[int]]):
	# m, n = len(inputMat), len(inputMat[0])
    # newmat: list[list[int]] = [[0 for _ in range(m)] for _ in range(n)]
    # for i in reversed(range(m)):
	# 	for j in range(n):
	# 		print(i, j)
	# 		print(j, m-i-1)

	# 		newmat[j][m-i-1] = inputMat[i][j]
	# 		print(inputMat[i][j], newmat[j][m-i-1])
	# 	print(newmat)
	# return newmat
    m, n = len(inputMat), len(inputMat[0])
    result = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][m-i-1] = inputMat[i][j]
    return result

def main():
	#input for inputMat
	inputMat = []
	inputMat_rows,inputMat_cols  = map(int, input().split())
	for idx in range(inputMat_rows):
		inputMat.append(list(map(int, input().split())))
	
	
	result = funcRotate(inputMat)
	print(result)	

main()