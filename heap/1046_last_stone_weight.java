class Solution {
    public int lastStoneWeight(int[] stones) {
   
        PriorityQueue<Integer> heap = new PriorityQueue(Collections.reverseOrder());
        
        for (int stone : stones) {
            heap.offer(stone);
        }
        
        while (heap.size() > 1) {
            int first = heap.poll();
            int second = heap.poll();

            if (first != second) {
                heap.offer((Math.abs(first - second)));
            } else if (first == second && heap.isEmpty()) {
                heap.offer(0);
            }
        }
        
        return heap.poll();
    }
}