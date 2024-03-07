class Solution {
    public int[] plusOne(int[] digits) {
         int n = digits.length;

        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }
        digits = new int[n+1];
        digits[0] = 1;
        return digits;

        // int n = digits.length;
        // int carry = 0;
        // for (int i = n - 1; i >= 0; i--) {
        //     if (i == n - 1) {
        //         if (digits[i] + 1 > 9) {
        //             digits[i] = 0;
        //             carry = 1;
        //         } else {
        //             digits[i] += 1;
        //         }
        //     } else if (carry == 1) {
        //         if (digits[i] + carry > 9) {
        //             digits[i] = 0;
        //             carry = 1;
        //         } else {
        //             digits[i] += 1;
        //             carry = 0;
        //         }
        //     }
        // }
        // if (carry == 1) {
        //     int[] res = new int[n+1];
        //     res[0] = 1;
        //     for (int i = 0; i < n; i++) {
        //         res[i + 1] = digits[i];
        //     }
        //     return res;
        // } else {
        //     return digits;
        // }
    }
}