class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deads = new HashSet();
        for (String deadend : deadends) {
            deads.add(deadend);
        }

        Set<String> seen = new HashSet();
        seen.add("0000");

        Queue<String> queue = new LinkedList();
        queue.offer("0000");
        queue.offer(null);

        int depth = 0;

        while (!queue.isEmpty()) {
            String node = queue.poll();

            if (node == null) {
                depth++;
                if (queue.peek() != null) {
                    queue.offer(null);
                }
            } else if (node.equals(target)) {
                return depth;
            } else if (!deads.contains(node)) {
                for (int i = 0; i < 4; i++) {
                    for (int d = -1; d <= 1; d += 2) {
                        int digit = ((node.charAt(i) - '0') + d + 10) % 10;
                        String neighbor = node.substring(0, i) + ("" + digit) + node.substring(i+1);
                        if (!seen.contains(neighbor)) {
                            seen.add(neighbor);
                            queue.offer(neighbor);
                        }
                    }
                }
            }
        }
        return -1;
        
    }
}