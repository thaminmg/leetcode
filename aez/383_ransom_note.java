class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int n1 = ransomNote.length();
        int n2 = magazine.length();
        if (n1 > n2) return false;

        Map<Character, Integer> hmap = new HashMap();
        for (int i = 0; i < n2; i++) {
            char c = magazine.charAt(i);
            hmap.put(c, hmap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < n1; i++) {
            char c = ransomNote.charAt(i);
            if (!hmap.containsKey(c) || hmap.get(c) <= 0) return false;
            hmap.put(c, hmap.getOrDefault(c, 0) - 1);
        }
        return true;
    }
}