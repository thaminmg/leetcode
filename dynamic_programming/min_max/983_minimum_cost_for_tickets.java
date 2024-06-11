class Solution {
    Set<Integer> daysSet = new HashSet();

    public int dfs(int[] dp, int[] days, int[] costs, int currDay) {
        if (currDay > days[days.length - 1]) return 0;
        if (!daysSet.contains(currDay)) {
            return dfs(dp, days, costs, currDay + 1);
        }
        if (dp[currDay] != - 1) return dp[currDay];

        int dayCost = costs[0] + dfs(dp, days, costs, currDay + 1);
        int weekCost = costs[1] + dfs(dp, days, costs, currDay + 7);
        int monthCost = costs[2] + dfs(dp, days, costs, currDay + 30);

        return dp[currDay] = Math.min(Math.min(dayCost, weekCost), monthCost);
    }

    public int mincostTicketsDFS(int[] days, int[] costs) {
        int lastDay = days[days.length - 1];
        int[] dp = new int[lastDay + 1];
        Arrays.fill(dp, - 1);

        for (int day : days) {
            daysSet.add(day);
        }

        return dfs(dp, days, costs, 1);
    }
    
    // =============================================================
    public int mincostTicketsBFS(int[] days, int[] costs) {
        int lastDay = days[days.length - 1];
        int[] dp = new int[lastDay + 1];
        Arrays.fill(dp, 0);

        int i = 0;
        for (int day = 1; day < lastDay + 1; day++) {
            if (days[i] > day) {
                dp[day] = dp[day - 1];
            } else {
                i++;
                dp[day] = Math.min(costs[0] + dp[day - 1],
                    Math.min(costs[1] + dp[Math.max(0, day - 7)],
                    costs[2] + dp[Math.max(0, day - 30)])
                );
            }
        }
        return dp[lastDay];
    }
}