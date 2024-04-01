class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        boolean flag = true;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (flag && s.charAt(i) == ' ') {
                continue;
            } else if (s.charAt(i) == ' ') {
                break;
            } else {
                res++;
                flag = false;
            }
        }
        return res;
    }
}