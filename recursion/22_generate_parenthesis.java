class Solution {
    List<String> res = new ArrayList();
    
    public void backtrack(StringBuilder curr, int leftCount, int rightCount, int n) {
        if (curr.length() == 2 * n) {
            res.add(curr.toString());
            return;
        }
        
        if (leftCount < n) {
            curr.append("(");
            backtrack(curr, leftCount + 1, rightCount, n);
            curr.deleteCharAt(curr.length() - 1);
        }
        if (rightCount < leftCount) {
            curr.append(")");
            backtrack(curr, leftCount, rightCount + 1, n);
            curr.deleteCharAt(curr.length() - 1);
        }
    }
    
    public List<String> generateParenthesis(int n) {
        backtrack(new StringBuilder(), 0, 0, n);
        return res;
    }
}