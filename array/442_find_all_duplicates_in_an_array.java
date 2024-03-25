class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();

        int n = nums.length;
        boolean[] seen = new boolean[n+1];

        for (int num : nums) {
            if (seen[num]){
               res.add(num);
               continue; 
            } 
            seen[num] = true;
        }
        return res;
    }
}