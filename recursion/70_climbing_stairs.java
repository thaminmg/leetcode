class Solution {
    HashMap<Integer, Integer> cache = new HashMap();
    
    public int climbStairs(int n) {
        if (cache.containsKey(n)) return cache.get(n);
        
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        int res = climbStairs(n - 1) + climbStairs(n - 2);
        
        cache.put(n, res);
        return res;
    }
}