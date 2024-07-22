class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n = heights.length;
        Integer[] sortedIndices = new Integer[n];

        for (int i = 0; i < n; i++) {
            sortedIndices[i] = i;
        }

        Arrays.sort(sortedIndices, (a, b) -> heights[b] - heights[a]);

        String[] res = new String[n];
        for (int i = 0; i < n; i++) {
            res[i] = names[sortedIndices[i]];
        }
        return res;
    }
}