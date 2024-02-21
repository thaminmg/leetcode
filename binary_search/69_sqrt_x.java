class Solution {
    public int mySqrt(int x) {
        if (x <= 1) return x;

        long left = 2, right = x / 2;

        while (left <= right) {
            long mid = left + (right - left) / 2;

            long temp = mid * mid;
            if (temp == x) {
                return (int) mid;
            } else if (temp > x) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return (int) right;
    }
}