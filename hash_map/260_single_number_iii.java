class Solution {
    public int[] singleNumber(int[] nums) {
        Map<Integer, Integer> hashmap = new HashMap();

        for (int num : nums) {
            hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
        }

        int[] res = new int[2];
        int i = 0;

        for (Map.Entry<Integer, Integer> item : hashmap.entrySet()) {
            if (item.getValue() == 1) {
                res[i++] = item.getKey();
            }
        }
        return res;
    }
}