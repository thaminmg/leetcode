class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersect(nums2, nums1);
        }

        HashMap<Integer, Integer> hmap = new HashMap();
        for (int num : nums1) {
            hmap.put(num, hmap.getOrDefault(num, 0) + 1);
        }
        int k = 0; 
        for (int num : nums2) {
            int cnt = hmap.getOrDefault(num, 0);
            if (cnt > 0) {
                nums1[k++] = num;
                hmap.put(num, cnt - 1);
            }
        }
        return Arrays.copyOfRange(nums1, 0, k);
    }
}