class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        return divideAndConquer(strs, 0, strs.length - 1);
    }
    
    public String divideAndConquer(String[] strs, int left, int right) {
        if (left == right) {
            return strs[left];
        }
        int mid = left + (right - left) / 2;
        String leftStr = divideAndConquer(strs, left, mid);
        String rightStr = divideAndConquer(strs, mid + 1, right);
        return combine(leftStr, rightStr);
    }
    
    public String combine(String left, String right) {
        int min = Math.min(left.length(), right.length());
        
        for (int i = 0; i < min; i++) {
            if (left.charAt(i) != right.charAt(i)) {
                return left.substring(0, i);
            }
        }
        return left.substring(0, min);
    }
}