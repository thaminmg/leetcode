class Solution {
    public int maximumWealth(int[][] accounts) {
        int res = 0;

        for (int[] acc : accounts) {
            int sum = Arrays.stream(acc).sum();
            res = Math.max(res, sum);
        }
        return res;
    }
}