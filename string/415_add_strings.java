class Solution {
    public String addStrings(String num1, String num2) {

        StringBuilder res = new StringBuilder();

        int carry = 0;
        int n1 = num1.length() - 1;
        int n2 = num2.length() - 1;
        while (n1 >= 0 || n2 >= 0) {

            int x = n1 >= 0 ? num1.charAt(n1) - '0' : 0;
            int y = n2 >= 0 ? num2.charAt(n2) - '0' : 0;
            int sum = (x + y + carry) % 10;
            carry = (x + y + carry) / 10;
            res.append(sum);
            n1--;
            n2--;
        }

        if (carry != 0) {
            res.append(carry);
        }
        
        return res.reverse().toString();
        
    }
}