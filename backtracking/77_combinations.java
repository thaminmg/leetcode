class Solution {
    
    List<List<Integer>> res = new ArrayList(); 
    int n;
    int k;
    
    public void backtrack(int value, List<Integer> curr) {
        if (curr.size() == k) {
            res.add(new ArrayList<>(curr));
            return;
        }
        
        for (int i = value; i <= n; i++) { 
            curr.add(i);
            backtrack(i + 1, curr);
            curr.remove(curr.size() - 1);
        }
    }
    
    public List<List<Integer>> combine(int n, int k) {
        this.n = n;
        this.k = k;
        
        backtrack(1, new ArrayList<>());
        return res;
    }
}