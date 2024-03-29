class KthLargest {

    PriorityQueue<Integer> heap;
    int size;
    public KthLargest(int k, int[] nums) {
        size = k;
        
        heap = new PriorityQueue();
        for (int num : nums) {
            heap.offer(num);
        }
        while (heap.size() > k) {
            heap.poll();
        }
    }
    
    public int add(int val) {
        heap.offer(val);
        if (heap.size() > size) {
            heap.poll();
        }
        return heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */