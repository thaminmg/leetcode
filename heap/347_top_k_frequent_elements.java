class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> hset = new HashMap();
        
        for (int num : nums) {
            if (hset.containsKey(num)) {
                int curr = hset.get(num);
                curr++;
                hset.put(num, curr);
            } else {
                hset.put(num, 1);
            }
        }
        
        PriorityQueue<Integer> heap = new PriorityQueue((n1, n2) -> hset.get(n1) - hset.get(n2));
        
        for (Map.Entry<Integer, Integer> entry : hset.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            
            heap.add(num);
            if (heap.size() > k) {
                heap.poll();
            }
        }

        int[] kTop = new int[k];
        for (int i = k - 1; i >= 0; i--) {
            kTop[i] = heap.poll();
        }
        return kTop;
    }
}