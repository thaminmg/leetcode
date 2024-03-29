class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        // O(n) + O(k)
        int n = nums.length;
        if (k > n) return nums;

        Deque<Integer> deque = new ArrayDeque<>();
        int[] res = new int[n - k + 1];
        int left = 0, right = 0, count = 0;

        while (right < n) {
            while (!deque.isEmpty() && nums[right] > nums[deque.peekLast()]) {
                deque.pollLast();
            }
            deque.offerLast(right);
            right++;
            if (left > deque.peekFirst()) deque.pollFirst();
            if (right >= k) {
                res[count++] = nums[deque.peekFirst()];
                left++;
            }
        }
        return res;


        // TLE
        // O(n^2) + O(n)
        // int n = nums.length;
        // if (k > n) return nums;
        
        // int[] res = new int[n - k + 1];
        // int[] min = new int[n]; 

        // for (int left = 0, right = 0; right < n; right++) {
        //     if (right < k) {
        //         res[0] = Math.max(nums[right], res[0]);
        //     } else {
        //         int start = ++left;
        //         int temp = Integer.MIN_VALUE;
        //         while (start < right) {
        //             temp = Math.max(nums[start], temp);
        //             start++;
        //         }
        //         res[right - k + 1] = Math.max(nums[right], temp);
        //     }
        // }
        // return res;     
    }
}