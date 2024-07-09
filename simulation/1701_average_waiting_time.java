class Solution {
    public double averageWaitingTime(int[][] customers) {
        int n = customers.length;
        long total = 0;
        int next = 0;

        for (int i = 0; i < n; i++) {
            int[] customer = customers[i];
            int startTime = customer[0];
            int duration = customer[1];

            next = Math.max(next, startTime) + duration;

            total += next - startTime;
        }
        
        return (double) total / n;
    }
}