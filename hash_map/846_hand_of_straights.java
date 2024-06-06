class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length;
        if (n % groupSize != 0) return false;

        Map<Integer, Integer> map = new TreeMap();
        for (int num : hand) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        while (map.size() > 0) {
            int smallest = map.entrySet().iterator().next().getKey();
            for (int i = 0; i < groupSize; i++) {
                if (!map.containsKey(smallest + i)) return false;
                map.put(smallest + i, map.get(smallest + i) - 1);

                if (map.get(smallest + i) == 0) {
                    map.remove(smallest + i);
                }
            }
        }
        return true;
    }
}