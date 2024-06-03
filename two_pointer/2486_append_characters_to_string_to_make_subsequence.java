class Solution {
    public int appendCharacters(String s, String t) {
        int m = s.length();
        int n = t.length();

        int left = 0, longest = 0;

        while (left < m && longest < n) {
            if (s.charAt(left) == t.charAt(longest)) {
                longest++;
            } 
            left++;
        }
        return n - longest;
    }
}