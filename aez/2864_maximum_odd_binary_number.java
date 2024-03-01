class Solution {
    public String maximumOddBinaryNumber(String s) {
        int ones = 0;
        int n = s.length();

        for (char c : s.toCharArray()) {
            if (c == '1') {
                ones++;
            }
        }

        StringBuilder strBuilder = new StringBuilder();
        ones--;
        while (n > 1) {
            if (ones > 0) {
                strBuilder.append("1");
                ones--;
            } else {
                strBuilder.append("0");
            }
            n--;
        }

        return strBuilder.append("1").toString();
    }
}