class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        return divideAndConquer(buildings, 0, buildings.length - 1);
    }
    
    public List<List<Integer>> divideAndConquer(int[][] buildings, int left, int right) {
        
        if (left == right) {
            List<List<Integer>> res = new ArrayList<>();
            res.add(Arrays.asList(buildings[left][0], buildings[left][2]));
            res.add(Arrays.asList(buildings[left][1], 0));
            return res;
        }
        
        int mid = left + (right - left) / 2;
        
        List<List<Integer>> leftSkyline = divideAndConquer(buildings, left, mid);
        List<List<Integer>> rightSkyline = divideAndConquer(buildings, mid + 1, right);
        return mergeSkylines(leftSkyline, rightSkyline);
    }
    
    public List<List<Integer>> mergeSkylines(List<List<Integer>> leftSkyline, List<List<Integer>> rightSkyline) {
        int leftPos = 0, rightPos = 0;
        int leftPrevHeight = 0, rightPrevHeight = 0;
        int currX, currY;
        List<List<Integer>> res = new ArrayList<>();
        
        while (leftPos < leftSkyline.size() && rightPos < rightSkyline.size()) {
            int nextLeftX = leftSkyline.get(leftPos).get(0);
            int nextRightX = rightSkyline.get(rightPos).get(0);
            
            if (nextLeftX < nextRightX) {
                leftPrevHeight = leftSkyline.get(leftPos).get(1);
                currX = nextLeftX;
                currY = Math.max(leftPrevHeight, rightPrevHeight);
                leftPos++;
            } else if (nextLeftX > nextRightX) {
                rightPrevHeight = rightSkyline.get(rightPos).get(1);
                currX = nextRightX;
                currY = Math.max(leftPrevHeight, rightPrevHeight);
                rightPos++;
            } else {
                leftPrevHeight = leftSkyline.get(leftPos).get(1);
                rightPrevHeight = rightSkyline.get(rightPos).get(1);
                currX = nextLeftX;
                currY = Math.max(leftPrevHeight, rightPrevHeight);
                leftPos++;
                rightPos++;
            }
            
            if (res.isEmpty() || res.get(res.size() - 1).get(1) != currY) {
                res.add(Arrays.asList(currX, currY));
            }
        }
        
        while (leftPos < leftSkyline.size()) {
            res.add(leftSkyline.get(leftPos++));
        }
        
        while (rightPos < rightSkyline.size()) {
            res.add(rightSkyline.get(rightPos++));
        }
        
        return res;
    }
}