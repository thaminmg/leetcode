class Solution {
    public int largestAltitude(int[] gain) {
        int sum = 0, res = 0;

        for (int i = 0; i < gain.length; i++) {
            sum += gain[i];
            res = Math.max(res, sum);
        }
        return res;
    }
}