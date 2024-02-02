class Solution {
    public void dfs(int[][] image, int sr, int sc, int from, int color) {
        int m = image.length, n = image[0].length;
        if (sr < 0 || sc < 0 || sr >= m || sc >= n || image[sr][sc] != from) return;
       
        image[sr][sc] = color;
        dfs(image, sr + 1, sc, from, color);
        dfs(image, sr, sc + 1, from, color);
        dfs(image, sr - 1, sc, from, color);
        dfs(image, sr, sc - 1, from, color);        
        
    }
    
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] != color) {
            dfs(image, sr, sc, image[sr][sc], color);
        }
        return image;
    }
}