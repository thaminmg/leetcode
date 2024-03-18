class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int total = 0;
        int curr = 0;
        int start = 0;
        for (int i = 0; i < n; i++) {
            total += gas[i] - cost[i];
            curr += gas[i] - cost[i];
            if (curr < 0) {
                start = i + 1;
                curr = 0;
            }
        }
        return total >= 0 ? start : - 1;

        // int n = gas.length;
        // for (int i = 0; i < n; i++) {
        //     int visited = 0, j = i, total = 0;

        //     while (visited < n) {
        //         total += gas[j % n] - cost[j % n];
        //         if (total < 0) break;
        //         visited++;
        //         j++;
        //     }
        //     if (visited == n && total >= 0) return i;
        // }
        // return -1;
    }
}
