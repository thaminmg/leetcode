class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) return 0;
            if (a[0] < b[0]) return -1;
            return 1;
        });
        
        List<int[]> ans = new ArrayList<>();

        int n = intervals.length;
        int stopCount = 0;
        int i = 1;

        ans.add(intervals[0]);

        while (i < n) {
            int[] curr = intervals[i];
            int[] prev = ans.get(ans.size() - 1);

            if (curr[0] <= prev[1]) {
                int min = Math.min(curr[0], prev[0]);
                int max = Math.max(curr[1], prev[1]);
                prev[0] = min;
                prev[1] = max;
            } else {
                ans.add(curr);
            }
            i++;
        }

        int[][] res = new int[ans.size()][2];

        for (int j = 0; j < ans.size(); j++) {
            res[j] = ans.get(j);
        }
        return res;
    }
}