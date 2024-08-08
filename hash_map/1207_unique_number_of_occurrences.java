class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> hset = new HashMap<>();

        for (int num : arr) {
            hset.put(num, hset.getOrDefault(num, 0) + 1);
        }

        Set<Integer> set = new HashSet<>(hset.values());
        return hset.size() == set.size();
    }
}