class Solution {
    private int[] binarySearch(int[][] intervals, int index) {
        int left = 0;
        int right = intervals.length - 1;
        int target = intervals[index][1];

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (intervals[mid][0] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        if (intervals[left][0] >= target) {
            return intervals[left];
        }
        return null;
    }

    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;

        int[] res = new int[n];
        HashMap<int[], Integer> hash = new HashMap<int[], Integer>();


        for (int i = 0; i < n; i++) {
            hash.put(intervals[i], i);
        }

        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        for (int i = 0; i < n; i++) {
            int[] interval = binarySearch(intervals, i);
            res[hash.get(intervals[i])] = interval == null ? -1 : hash.get(interval);
        }
        return res;
    }
}