def edit_distance_with_transposition(S, T):
    m, n = len(S), len(T)
    
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][n] = m - i
    for j in range(n + 1):
        dp[m][j] = n - j
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if S[i] == T[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 +  min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j + 1])           
            if i + 1 < m and j + 1 < n and S[i] == T[j + 1] and S[i + 1] == T[j]:
                dp[i][j] = min(dp[i][j], dp[i + 1][j + 1] + 1)  # Transposition
    edit_distance = dp[0][0]
    return edit_distance

S = "CTAC"
T = "GCTCA"
distance = edit_distance_with_transposition(S, T)
print("Edit Distance:", distance)
