class Solution {
    public int calPoints(String[] operations) {
        List<Integer> res = new ArrayList();

        for (String op : operations) {
            if (op.equals("+")) {
                res.add(res.get(res.size() - 1) + res.get(res.size() - 2));
            } else if (op.equals("D")) {
                res.add(res.get(res.size() - 1) * 2);
            } else if (op.equals("C")) {
                res.remove(res.size() - 1);
            } else {
                res.add(Integer.parseInt(op));
            }
        }
        int ans = 0;
        for (int i = 0; i < res.size(); i++) {
            ans += res.get(i);
        }
        return ans;
    }
}