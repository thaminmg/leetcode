class Solution {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex == 0) return Arrays.asList(1);
        if (rowIndex == 1) return Arrays.asList(1, 1);
        
        List<Integer> above = getRow(rowIndex - 1);
        List<Integer> res = new ArrayList();
        res.add(1);
        
        for (int i = 0; i < above.size() - 1; i++) {
            res.add(above.get(i) + above.get(i+1));
        }
        res.add(1);
        return res;
    }
}