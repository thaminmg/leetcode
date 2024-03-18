class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) return 0;

        int res = 1;
        Arrays.sort(points, (p1, p2) -> {
            if (p1[1] == p2[1]) return 0;
            if (p1[1] < p2[1]) return -1;
            return 1;
        });

        int start, end, prevEnd = points[0][1];
        for (int[] pt : points) {
            start = pt[0];
            end = pt[1];

            if (prevEnd < start) {
                res++;
                prevEnd = end;
            }
        }
        return res;
    }
}