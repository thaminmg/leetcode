class Solution {
    
    HashMap<Integer, Integer> cache = new HashMap();
    
    public int fib(int n) {
        if (cache.containsKey(n)) return cache.get(n);
        
        if (n < 2) return n;
        
        int res = fib(n-1) + fib(n-2);
        
        cache.put(n, res);
        return res;
    }
}