class Solution {
    public double average(int[] salary) {
        int n = salary.length;
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        int res = 0;

        for (int s : salary) {
            max = Math.max(max, s);
            min = Math.min(min, s);
            res += s;
        }
        return (double) (res - min - max) / (n - 2);
    }
}