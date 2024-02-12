class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hset = new HashMap();
        int res = 0;

        for (int num : nums) {
            int count = hset.getOrDefault(num, 0) + 1;
            int resMax = hset.getOrDefault(res, 0);
            hset.put(num, count); 
            res = count >= resMax ? num : res; 
        }
        return res;
    }
}