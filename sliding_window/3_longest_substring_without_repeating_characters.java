class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] map = new int[128];
        int left = 0, right = 0, counter = 0, res = 0;
        while (right < s.length()) {
            char temp = s.charAt(right);
            if (++map[temp] > 1) counter++;
            right++;

            while (counter > 0) {
                char leftC = s.charAt(left);
                if (map[leftC]-- > 1) counter--;
                left++;
            }
            res = Math.max(res, right - left);
        }
        return res;
    }
}