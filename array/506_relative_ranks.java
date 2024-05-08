class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        int[] copy = new int[n];
        System.arraycopy(score, 0, copy, 0, n);

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(copy[i], i);
        }

        Arrays.sort(copy);

        String[] res = new String[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                res[map.get(copy[n - i - 1])] = "Gold Medal";
            } else if (i == 1) {
                res[map.get(copy[n - i - 1])] = "Silver Medal";
            } else if (i == 2) {
                res[map.get(copy[n - i - 1])] = "Bronze Medal";                
            } else {
                res[map.get(copy[n - i - 1])] = Integer.toString(i+1);
            }
        }
        return res;
    }
}