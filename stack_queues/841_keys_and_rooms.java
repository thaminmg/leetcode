class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        int[] res = new int[n];
        
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<Integer>();
        queue.offer(0);
        visited.add(0);

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            
            for (int j = 0; j < rooms.get(curr).size(); j++) {
                if (!visited.contains(rooms.get(curr).get(j))) {
                    visited.add(rooms.get(curr).get(j));
                    res[rooms.get(curr).get(j)] = 1;
                    queue.offer(rooms.get(curr).get(j));
                }
            }

        }
        return n == Arrays.stream(res).sum() + 1;
        
    }
}