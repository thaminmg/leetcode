class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet();
        Set<Integer> s2 = new HashSet();
        List<List<Integer>> res = new ArrayList();

        res.add(new ArrayList<Integer>());
        res.add(new ArrayList<Integer>());


        for (int num : nums1) s1.add(num);
        for (int num : nums2) s2.add(num);

        for (int num : s1) {
            if (!s2.contains(num)) res.get(0).add(num);
        }

        for (int num : s2) {
            if (!s1.contains(num)) res.get(1).add(num);
        }

        return res;
    }
}