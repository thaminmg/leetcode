class Solution {
    public int findNumbers(int[] nums) {
        int res = 0;
        
        for (int num : nums) {
            int count = (int) Math.floor(Math.log10(num)) + 1;
            if ((count & 1) == 0) res++;
        }
        
        return res;
    }
}
