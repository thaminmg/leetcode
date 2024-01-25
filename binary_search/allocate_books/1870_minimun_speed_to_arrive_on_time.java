class Solution {

    private double allocate(int[] dist, int limit) {
        double count = 0.0;
        for (int i = 0; i < dist.length; i++) {
            double time = (double) dist[i] / (double) limit;
            count += ( i == dist.length - 1 ? time : Math.ceil(time));
        }
        return count;
    }

    public int minSpeedOnTime(int[] dist, double hour) {
        int left = 1;
        int right = 1000000000;
       
        int speed = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            double count = allocate(dist, mid);

            if (count <= hour) {
                speed = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return speed;
    }
}