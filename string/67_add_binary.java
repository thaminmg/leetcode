class Solution {
    public String addBinary(String a, String b) {
        int m = a.length();
        int n = b.length();
        if (m < n) return addBinary(b, a);
        
        int carry = 0;
        int j = n - 1;
        StringBuilder sb = new StringBuilder();
        
        for (int i = m - 1; i >= 0; i--) {
            if (a.charAt(i) == '1') carry++;
            if (j > -1 && b.charAt(j--) == '1') carry++;
            
            if ((carry & 1) == 1) {
                sb.append('1');
            }
            else {
                sb.append('0');
            }
            carry /= 2;
        }
        if (carry == 1) {
            sb.append('1');
        }
        return sb.reverse().toString();
    }
}