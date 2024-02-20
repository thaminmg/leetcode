class Solution {
    
    public int[] countingSort(int[] arr) {
        
        int shift = Arrays.stream(arr).min().getAsInt();
        int k = Arrays.stream(arr).max().getAsInt() - shift;
        
        int[] counts = new int[k + 1];
        for (int num: arr) {
            counts[num - shift] += 1;
        }
        
        int startingIndex = 0;
        for (int i = 0; i < k + 1; i++) {
            int count = counts[i];
            counts[i] = startingIndex;
            startingIndex += count;
        }
        
        int[] res = new int[arr.length];
        for (int num: arr) {
            res[counts[num - shift]] = num;
        }
        return res;
        
    }
    
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        int[] sortedArr = countingSort(arr);
    
        int minAbs = Integer.MAX_VALUE;
        
        for (int i = 1; i < sortedArr.length; i++) {
            minAbs = Math.min(minAbs, sortedArr[i] - sortedArr[i-1]);
        }
        
        List<List<Integer>> res = new ArrayList();
        
        for (int i = 1; i < sortedArr.length; i++) {
            if(minAbs == sortedArr[i] - sortedArr[i-1]) {
                res.add(Arrays.asList(sortedArr[i-1], sortedArr[i]));   
            }
        }
        return res;
    }
}