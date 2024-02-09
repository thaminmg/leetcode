class Solution {
    public int heightChecker(int[] heights) {
        boolean isSwapped = true;
        int res = 0;
        int[] originals = heights.clone();
        
        while (isSwapped) {
            isSwapped = false;
            for (int i = 0; i < heights.length - 1; i++) {
                if (heights[i] > heights[i+1]) {
                    int temp = heights[i];
                    heights[i] = heights[i+1];
                    heights[i+1] = temp;
                    isSwapped = true;
                }
            }
        }
        
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != originals[i]) res++;
        }
        return res;
    }
}