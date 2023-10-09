def find_longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n  
    max_length = 1
    end_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                if dp[i] > max_length:
                    max_length = dp[i]
                    end_index = i

    # Reconstruct the LIS
    lis = []
    lis.append(nums[end_index])
    current_length = max_length - 1
    for i in range(end_index - 1, -1, -1):
        if dp[i] == current_length and nums[i] < lis[-1]:
            lis.append(nums[i])
            current_length -= 1

    return lis

# Example usage
sequence = [3, 2, 5, 1, 6, 3, 9, 2]
longest_increasing_subsequence = find_longest_increasing_subsequence(sequence)
print("Longest Increasing Subsequence:", longest_increasing_subsequence)
