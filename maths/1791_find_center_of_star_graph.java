class Solution {

    public int findCenter(int[][] edges) {
        Map<Integer, Integer> hashMap = new HashMap();

        for (int[] edge : edges) {
            hashMap.put(edge[0], hashMap.getOrDefault(edge[0], 0) + 1);
            hashMap.put(edge[1], hashMap.getOrDefault(edge[1], 0) + 1);
        }

        for (int node : hashMap.keySet()) {
            if (hashMap.get(node) == edges.length) {
                return node;
            }
        }
        return -1;
    }
}