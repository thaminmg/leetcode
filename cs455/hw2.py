# def count_pairs(A, T):
#     def merge(left, right):
#         return sorted(left + right)

#     def recursion(arr):
#         if len(arr) <= 1:
#             return 0, arr
#         half = len(arr) // 2
#         left_ans, left = recursion(arr[:half])
#         right_ans, right = recursion(arr[half:])
#         cross_ans = 0
#         j = 0
#         for i in range(len(left)):
#             while j < len(right) and left[i] - right[j] >= T:
#                 j += 1
#             cross_ans += j
#         return left_ans + cross_ans + right_ans, merge(left, right)

#     ans, _ = recursion(A)
#     return ans

# A = [2, 7, 14, 22, 30, 37, 43, 50, 57, 63, 71, 78, 85, 91, 98, 105, 112, 118, 125, 133]
# T = 8
# print(count_pairs(A,T))
def count_pairs_with_threshold(arr, T):
    def merge_count(left, mid, right):
        count = 0
        i, j = left, mid + 1
        
        while i <= mid:
            while j <= right and arr[j] - arr[i] < T:
                j += 1
            count += (j - mid - 1)
            i += 1
        return count
    
    def dc_count(left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        lcount = dc_count(left, mid)
        rcount = dc_count(mid + 1, right)
        mcount = merge_count(left, mid, right)
        return lcount + rcount + mcount
    
    return dc_count(0, len(arr) - 1)

# Example usage
A = [2, 7, 14, 22, 30, 37, 43, 50, 57, 63, 71, 78, 85, 91, 98, 105, 112, 118, 125, 133]
T = 8
result = count_pairs_with_threshold(A, T)
print("Number of pairs (i, j) where (A[j] - A[i]) < T:", result)

# def count_pairs_with_threshold_bruteforce(arr, T):
#     count = 0
#     n = len(arr)

#     # Iterate through all possible pairs of indices (i, j) where i < j
#     for i in range(n):
#         for j in range(i + 1, n):
#             # Calculate the difference between A[j] and A[i]
#             diff = arr[j] - arr[i]
            
#             # If the difference is less than T, increment the count
#             if diff < T:
#                 count += 1

#     return count

# # Example usage
# A = [2, 7, 14, 22, 30, 37, 43, 50, 57, 63, 71, 78, 85, 91, 98, 105, 112, 118, 125, 133]
# T = 8
# result = count_pairs_with_threshold_bruteforce(A, T)
# print("Number of pairs (i, j) where (A[j] - A[i]) < T:", result)
