class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        int n = happiness.length;
        Integer[] copy = new Integer[n];
        for (int i = 0; i < n; i++) {
            copy[i] = happiness[i];
        }

        Arrays.sort(copy, Collections.reverseOrder());

        long res = 0;
        int turns = 0;

        for (int i = 0; i < k; i++) {
            res += Math.max(copy[i] - turns, 0);
            turns++;
        }
        return res;
    }
}