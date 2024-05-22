class Solution {
    int n = 0;
    String s;

    List<List<String>> res = new ArrayList<List<String>>();
    
    public boolean isPalindrome(int left, int right) {
        while (left < right) {
            if (this.s.charAt(left++) != this.s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }

    public void dfs(int start, List<String> curr) {
        if (start >= n) {
            res.add(new ArrayList<String>(curr));
        }
        for (int end = start; end < n; end++) {
            if (isPalindrome(start, end)) {
                curr.add(this.s.substring(start, end + 1));
                dfs(end + 1, curr);
                curr.remove(curr.size() - 1);
            }
        }

    }

    public List<List<String>> partition(String s) {
        n = s.length();
        this.s = s;
        
        dfs(0, new ArrayList<String>());        
        return res;
    }
}