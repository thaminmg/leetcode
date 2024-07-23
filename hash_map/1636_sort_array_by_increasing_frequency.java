class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> hset = new HashMap();

        for (int num : nums) {
            hset.put(num, hset.getOrDefault(num, 0) + 1);
        }

        Integer[] freq = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            freq[i] = nums[i];
        }

        Arrays.sort(freq, (a, b) -> {
            if (hset.get(a).equals(hset.get(b))) {
                return Integer.compare(b, a);
            }
            return Integer.compare(hset.get(a), hset.get(b));
        });

        for (int i = 0; i < nums.length; i++) {
            nums[i] = freq[i];
        }
        return nums;
    }
}