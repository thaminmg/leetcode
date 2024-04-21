class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> hset = new HashMap();

        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];

            hset.computeIfAbsent(a, val -> new ArrayList<Integer>()).add(b);
            hset.computeIfAbsent(b, val -> new ArrayList<Integer>()).add(a);
        }

        boolean[] visited = new boolean[n];
        visited[source] = true;
        Stack<Integer> stack = new Stack();
        stack.push(source);

        while (!stack.isEmpty()) {
            int curr = stack.pop();
            if (curr == destination) return true;

            for (int next : hset.get(curr)) {
                if (!visited[next]) {
                    visited[next] = true;
                    stack.push(next);
                }
            }
        }
        return false;
    }
}