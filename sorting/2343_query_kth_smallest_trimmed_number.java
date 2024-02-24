class Solution {
//     private final int NUM_DIGITS = 10;
    
//     public void helper(String[] nums, int placeValue, int idx){
//         int[] counts = new int[NUM_DIGITS];
//         for (String num : nums) {
//             int current = Character.getNumericValue(num.charAt(idx));
//             // int current = intNum / placeValue;
//             counts[current % NUM_DIGITS] += 1;
//         }
        
//         int startingIndex = 0;
//         for (int i = 0; i < counts.length; i++) {
//             int count = counts[i];
//             counts[i] = startingIndex;
//             startingIndex += count;
//         }
        
//         String[] sortedArr = new String[nums.length];
//         for (String num : nums) {
//             int current = Character.getNumericValue(num.charAt(idx));
            
//             // int current = intNum / placeValue;
//             sortedArr[counts[current % NUM_DIGITS]] = num;
//             counts[current % NUM_DIGITS] += 1;
//         }
        
//         for (int i = 0; i < nums.length; i++) {
//             nums[i] = sortedArr[i];
//         }
//     }
    
//     public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        
//         HashMap<String, Integer> map = new HashMap();
//         for (int i = 0; i < nums.length; i++) {
//             map.put(nums[i], i);
//         }
//         int[] res = new int[queries.length];
        
//         for (int i = 0; i < queries.length; i++) {
//             int k = queries[i][0] - 1;
//             int toRight = queries[i][1];
            
//             int placeValue = 1;
//             String[] arr = Arrays.copyOfRange(nums, 0, nums.length);
            
//             int j = 0;
//              while (toRight > 0) {
//                 helper(arr, placeValue, j);
//                  placeValue *= 10;
//                  j++;
//                  toRight--;
//              }

//             res[i] = map.get(arr[k]);
//         }
//         return res;
//     }
    public int[] smallestTrimmedNumbers(String[] nums, int[][] queries) {
        int n = queries.length, j = 0;
        int[] ans = new int[n];
        Map<Integer, String[][]> trimmed = new HashMap<>();
        for (int[] q : queries) {
            int k = q[0] - 1;
            int trim = q[1];
            if (!trimmed.containsKey(trim)) {
                String[][] arr = new String[nums.length][2];
                int i = 0;
                for (String num : nums) {
                    int sz = num.length();
                    arr[i] = new String[]{num.substring(sz - trim), "" + i++};
                }
                Arrays.sort(arr, Comparator.comparing(a -> a[0]));
                trimmed.put(trim, arr);
            }
            ans[j++] = Integer.parseInt(trimmed.get(trim)[k][1]);
        }
        return ans;        
    }
}
