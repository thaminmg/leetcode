class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<int[]>(Comparator.comparingDouble(a -> (double) a[0] / a[1]));
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                minHeap.offer(new int[]{arr[i], arr[j]});
            }
        }

        int[] res = null;
        for (int i = 0; i < k; i++) {
            res = minHeap.poll();
        }
        return res;
    }
}