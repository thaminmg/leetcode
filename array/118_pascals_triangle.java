class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(Arrays.asList(1));
        if (numRows == 1) {
            return res;
        }
        
        for (int i = 1; i < numRows; i++) {
            List<Integer> prev = res.get(res.size() - 1);
            int prevSize = prev.size();
            List<Integer> temp = new ArrayList<>();
            temp.add(1);
            for (int j = 0; j < prevSize - 1; j++) {
                temp.add(prev.get(j) + prev.get(j+1));
            }
            temp.add(1);
            res.add(temp);
        }
        return res;
    }
    
}