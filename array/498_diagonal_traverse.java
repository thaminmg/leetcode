class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        int[] res = new int[m * n];
        List<Integer> temp = new ArrayList<>();
        int k = 0;
        for (int i = 0; i < m + n - 1; i++) {
            temp.clear();
            int r = i < n ? 0 : i - n + 1;
            int c = i < n ? i : n - 1;
            
            while (r < m && c > -1) {
                temp.add(mat[r][c]);
                r++;
                c--;
            }
            
            if ((i & 1) == 0) {
                Collections.reverse(temp);
            }
            
            for (int j = 0; j < temp.size(); j++) {
                res[k++] = temp.get(j);
            }
        }

        return res;
    }
}