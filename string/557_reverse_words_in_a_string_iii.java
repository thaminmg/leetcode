class Solution {
    public String reverseWords(String s) {
        int left = 0, right = 0, n = s.length();
        char[] res = s.toCharArray();
        while (left < n) {
            while (right < n && res[right] != ' ') {
                right++;
            }
            reverse(res, left, right - 1);
            left = right + 1;
            right = left;
        }
        return new String(res);
    }
    
    public void reverse(char[] res, int start, int end) {
        while (start < end) {
            char temp = res[start];
            res[start] = res[end];
            res[end] = temp;
            start++;
            end--;
        }
    }
}