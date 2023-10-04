from typing import Tuple


def findIndices(n: list[int], x: int) -> list[int]: 
	res: list[int] = []
	for idx, val in enumerate(n):
		if val == x:
			res.append(idx)
	return res
			 
# n = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
# x = 1
# print(findIndices(n, x))

# n = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 1
# print(findIndices(n, x))


def findMaximumDifferenceBruteForce(Y: list[int]) -> tuple[int, int]:
	res: tuple[int, int] = (0, 0)
	max_val: int = 0
	for i in range(len(Y) - 1):
		for j in range(i + 1, len(Y)):
			temp = (j - i) * min(Y[i], Y[j])
			if temp > max_val:
				res = (i, j)
				max_val = temp			
	return res
	
X = [8, 4, 1]
print(findMaximumDifferenceBruteForce(X))

Y = [10, 3, 8, 4, 19, 7, 12]
print(findMaximumDifferenceBruteForce(Y))

Z = [5, 9, 3, 10, 4, 7, 11]
print(findMaximumDifferenceBruteForce(Z))


def findMaximumDifferenceOptimal(Y: list[int]) -> tuple[int, int]:
    i: int = 0
    j: int = len(Y) - 1
    max_val: int = 0
    res: tuple[int, int] = (0, 0)

    while i < j:
        temp = (j - i) * min(Y[i], Y[j])
        if temp > max_val:
            max_val = temp
            res = (i, j)
        if Y[i] < Y[j]:
            i += 1
        else:
            j -= 1
    return res

print(findMaximumDifferenceOptimal(X))
print(findMaximumDifferenceOptimal(Y))
print(findMaximumDifferenceOptimal(Z))


# def max_A(Y):
#     left = 0
#     right = len(Y) - 1
#     max_A = 0
#     max_pair = (0, 0)

#     while left < right:
#         A = (right - left) * min(Y[left], Y[right])
#         if A > max_A:
#             max_A = A
#             max_pair = (left, right)

#         if Y[left] < Y[right]:
#             left += 1
#         else:
#             right -= 1

#     return max_pair

# def max(Y):
# 	n = len(Y)
# 	max_value = max(Y)
# 	max_indices = (0, 0)

# 	for i in range(n):
# 		if Y[i] == max_value:
# 			left_index = i - 1
# 			right_index = i + 1
# 			while left_index >= 0 and Y[left_index] >= max_value:
# 				left_index -= 1
# 			while right_index < n and Y[right_index] >= max_value:
# 				right_index += 1
			
# 			A_ij = (right_index - left_index - 2) * max_value

# 			if A_ij > max_A:
# 				max_A = A_ij
# 				max_indices = (left_index + 1, right_index - 1)
# 	return max_indices

# print(max_A(X))
# print(max_A(Y))
# print(max_A(Z))