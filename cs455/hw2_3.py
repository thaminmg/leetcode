def edit_distance_with_transposition(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                cost = 0
            else:
                cost = 1
            
            dp[i][j] = min(
                dp[i - 1][j] + 1,    
                dp[i][j - 1] + 1,    
                dp[i - 1][j - 1] + cost  
            )
            
            if i > 1 and j > 1 and S[i - 1] == T[j - 2] and S[i - 2] == T[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)  
    edit_distance = dp[m][n]
    
    return edit_distance

S = "CTAC"
T = "GCTCA"
print(edit_distance_with_transposition(S, T)) # prints 2
