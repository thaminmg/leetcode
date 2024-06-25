class Solution {
    public int dfs(String s, int index, Integer[] memo) {
        if (memo[index] != null) return memo[index];
        
        if (index == s.length()) return 1;
        if (s.charAt(index) == '0') return 0;
        if (index == s.length() - 1) return 1;
        
        int res = dfs(s, index + 1, memo);
        if (Integer.parseInt(s.substring(index, index + 2)) <= 26) {
            res += dfs(s, index + 2, memo);
        }
        return memo[index] = res;
    }
    
    public int numDecodings(String s) {
       Integer[] memo = new Integer[s.length() + 1];
        return dfs(s, 0, memo);
    }
}