class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        HashMap<Integer, Integer> res = new HashMap();
        
        for (int i = 0; i < mat.length; i++) {
            res.put(i, Arrays.stream(mat[i]).sum());    
        }
        
        PriorityQueue<Integer> heap = new PriorityQueue((n1, n2) -> {
             if (res.get(n1) != res.get(n2)) {
                return Integer.compare(res.get(n1), res.get(n2));
            } else {
                return Integer.compare((Integer) n1, (Integer) n2);
            }
        });
        
        for (int i = 0; i < res.size(); i++) {
            heap.offer(i);
        }
        
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = heap.poll();
        }
        return ans;
    }
}