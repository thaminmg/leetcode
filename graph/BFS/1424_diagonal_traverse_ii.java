class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        Queue<Pair<Integer, Integer>> groups = new LinkedList();
        groups.offer(new Pair(0,0));

        List<Integer> res = new ArrayList();

        while(!groups.isEmpty()) {
            Pair<Integer, Integer> p = groups.poll();
            int row = p.getKey();
            int col = p.getValue();
            res.add(nums.get(row).get(col));

            if (col == 0 && row + 1 < nums.size()) {
                groups.offer(new Pair(row + 1, col));
            }

            if (col + 1 < nums.get(row).size()) {
                groups.offer(new Pair(row, col + 1));
            }
        }
        int[] ans = new int[res.size()];
        int i = 0;
        while (i < res.size()) {
            ans[i] = res.get(i);
            i++;
        }
        return ans;

        // Map<Integer, List<Integer>> groups = new HashMap();

        // int n = 0;

        // for (int row = nums.size()-1; row >= 0; row--) {
        //     for (int col = 0; col < nums.get(row).size(); col++) {
        //         int diagonal = row + col;

        //         if (!groups.containsKey(diagonal)) {
        //             groups.put(diagonal, new ArrayList<Integer>());
        //         }
        //         groups.get(diagonal).add(nums.get(row).get(col));
        //         n++;
        //     }
        // }

        // int[] res = new int[n];
        // int i = 0, curr = 0;
        // while (groups.containsKey(curr)) {
        //     for (int num : groups.get(curr)) {
        //         res[i++] = num;
        //     }
        //     curr++;
        // }
        // return res;
    }
}