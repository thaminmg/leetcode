class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        double res = Integer.MAX_VALUE * 1.0;

        List<Double> lst = new ArrayList();
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int min = nums[left++];
            int max = nums[right--];
            double mid = (min + max) / 2.0;

            lst.add(mid);
        }
        for (int i = 0; i < lst.size(); i++) {
            res = Math.min(res, lst.get(i));
        }
        return res;
    }
}