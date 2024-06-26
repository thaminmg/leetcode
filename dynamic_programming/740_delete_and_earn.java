class Solution {
    Map<Integer, Integer> points = new HashMap();
    Map<Integer, Integer> cache = new HashMap();

    public int maxPoints(int num) {
        if (num == 0) return 0;
        if (num == 1) return points.getOrDefault(1, 0);

        if (cache.containsKey(num)) return cache.get(num);

        int gain = points.getOrDefault(num, 0);
        cache.put(num, Math.max(maxPoints(num - 1), maxPoints(num - 2) + gain));
        return cache.get(num);
    }

    public int deleteAndEarn(int[] nums) {
        int maxNum = 0;

        for (int num : nums) {
            points.put(num, points.getOrDefault(num, 0) + num);
            maxNum = Math.max(maxNum, num);
        }
        return maxPoints(maxNum);
    }
}