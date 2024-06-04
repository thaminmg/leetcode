class Solution {
    int[] jobDifficulty;
    int n, d;
    int[][] memo;
    int[] hardestJobRemaining;
    
    public int dp(int i, int day) {

        if (day == d) {
            return hardestJobRemaining[i];
        }
        
        if (memo[i][day] == -1) {
            int best = Integer.MAX_VALUE;
            int hardest = 0;
            for (int j = i; j < n - (d - day); j++) {
                hardest = Math.max(hardest, jobDifficulty[j]);
                best = Math.min(best, hardest + dp(j + 1, day + 1));
            }
            memo[i][day] = best;
        }
        return memo[i][day];
    }
    
    public int minDifficulty(int[] jobDifficulty, int d) {
        
        this.n = jobDifficulty.length;
        if (n < d) return - 1;
        
        hardestJobRemaining = new int[n];
        int hardest = 0;
        for (int i = n - 1; i >= 0; i--) {
            hardest = Math.max(hardest, jobDifficulty[i]);
            hardestJobRemaining[i] = hardest;
        }
        
        memo = new int[n][d + 1];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        
        this.jobDifficulty = jobDifficulty;
        this.d = d;
    
        return dp(0, 1);
    }
}