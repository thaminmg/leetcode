class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
       int x1, x2, y1, y2, x3, y3;
       x1 = coordinates[0][0];
       y1 = coordinates[0][1];
       x2 = coordinates[1][0];
       y2 = coordinates[1][1];

       for (int i = 2; i < coordinates.length; i++) {
            x3 = coordinates[i][0];
            y3 = coordinates[i][1];

            if ((x2 - x1) * (y3 - y2) != (x3 - x2) * (y2 - y1)) return false;
       }  
       return true;
    }
}