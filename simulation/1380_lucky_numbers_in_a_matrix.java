class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;

        List<Integer> rowMin = new ArrayList();
        for (int i = 0; i < m; i++) {
            int rMin = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                rMin = Math.min(rMin, matrix[i][j]);
            }
            rowMin.add(rMin);
        }

        List<Integer> colMax = new ArrayList();
        for (int i = 0; i < n; i++) {
            int cMax = Integer.MIN_VALUE;
            for (int j = 0; j < m; j++) {
                cMax = Math.max(cMax, matrix[j][i]);
            }
            colMax.add(cMax);
        }

        List<Integer> res = new ArrayList();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == rowMin.get(i) && matrix[i][j] == colMax.get(j)) {
                    res.add(matrix[i][j]);
                }
            }
        }
        return res;
    }
}