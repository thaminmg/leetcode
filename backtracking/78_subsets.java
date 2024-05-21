class Solution {
    int n = 0;
    int k;
    int[] nums = null;
    List<List<Integer>> res = new ArrayList();

    public void backtrack(int ptr, List<Integer> curr) {
        if (curr.size() == k) {
            res.add(new ArrayList(curr));
            return;
        }
        for (int i = ptr; i < n; i++) {
            curr.add(this.nums[i]);
            backtrack(i + 1, curr);
            curr.remove(curr.size() - 1);
        }
    }
    public List<List<Integer>> subsets(int[] nums) {
        n = nums.length;
        this.nums = nums;

        for (k = 0; k < n + 1; k++) {
            backtrack(0, new ArrayList<Integer>());
        }
        return res;
    }
}