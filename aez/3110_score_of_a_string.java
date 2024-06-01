class Solution {
    public int scoreOfString(String s) {
        int res = 0;

        for (int i = 1; i < s.length(); i++) {
            int first = (int) (s.charAt(i - 1));
            int second = (int) (s.charAt(i));
           
            res += Math.abs(second - first);
        }
        return res;
    }
}