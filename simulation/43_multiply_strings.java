class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";

        int m = num1.length(), n = num2.length();
        int[] res = new int[m + n];

        for (int i = m - 1; i >= 0; i--) {
            int a = num1.charAt(i) - '0';
            for (int j = n - 1; j >= 0; j--) {
                int b = num2.charAt(j) - '0';
                res[i + j + 1] += a * b;
            }
        }

        for (int k = res.length - 1; k > 0; k--) {
            res[k - 1] += res[k] / 10;
            res[k] %= 10;
        }
        
        StringBuilder ans = new StringBuilder();
        int index = res[0] == 0 ? 1 : 0;
        for (; index < res.length; index++) {
            ans.append(res[index]);
        }

        return ans.toString();
    }
}

        // if (num1.equals("0") || num2.equals("0")) return "0";
        // StringBuilder s1 = new StringBuilder(num1);
        // StringBuilder s2 = new StringBuilder(num2);
        // s1.reverse();
        // s2.reverse();

        // int N = num1.length() + num2.length();
        // StringBuilder res = new StringBuilder();
        // for (int i = 0; i < N; i++) res.append(0);

        // for (int d2 = 0; d2 < s2.length(); d2++) {
        //     int digit2 = s2.charAt(d2) - '0';

        //     for (int d1 = 0; d1 < s1.length(); d1++) {
        //         int digit1 = s1.charAt(d1) - '0';

        //         int currPos = d1 + d2;
        //         int carry = res.charAt(currPos) - '0';
        //         int product = digit1 * digit2 + carry;

        //         res.setCharAt(currPos, (char) (product % 10 + '0'));
                
        //         int nextCarry = res.charAt(currPos + 1) - '0' + product / 10;
        //         res.setCharAt(currPos + 1, (char) (nextCarry + '0'));
        //     }
        // }

        // if (res.charAt(res.length() - 1) == '0') {
        //     res.deleteCharAt(res.length() - 1);
        // }
        // res.reverse();
        // return res.toString();
