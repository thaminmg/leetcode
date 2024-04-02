class Solution {
    public String transformString(String s) {
        Map<Character, Integer> hash = new HashMap<>();

        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!hash.containsKey(c)) {
                hash.put(c, i);
            }
            sb.append(hash.get(c) + "");
            sb.append(" ");
        }
        return sb.toString();

    public boolean isIsomorphic(String s, String t) {
        int sn = s.length(), tn = t.length();
        if (sn != tn) return false;

        return transformString(s).equals(transformString(t));
    }
}