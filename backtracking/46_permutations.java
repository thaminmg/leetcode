class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    int[] nums;
    public void backtrack(List<Integer> curr) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<Integer>(curr));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (curr.contains(nums[i])) continue;
            
            curr.add(nums[i]);
            backtrack(curr);
            curr.remove(curr.size() - 1);
        }
    }
    
    public List<List<Integer>> permute(int[] nums) {
        this.nums = nums;
        
        backtrack(new ArrayList<Integer>());
        
        return res;
    }
}