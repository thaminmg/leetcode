class Solution {
    public String minWindow(String s, String t) {
        int[] map = new int[128];

        for (char c : t.toCharArray()) {
            map[c]++;
        }

        int left = 0, right = 0, minLen = Integer.MAX_VALUE, start = 0, counter = t.length();
    
        while (right < s.length()) {
            char temp = s.charAt(right);

            if (map[temp] > 0) {
                counter--;
            }
            map[temp]--;
            right++;
            
            while (counter == 0) {
                if (minLen > right - left) {
                    minLen = right - left;
                    start = left;
                }
                char leftC = s.charAt(left);
                if (++map[leftC] > 0) counter++;
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);

        // int sn = s.length(), tn = t.length();
        // String res = "";
        // if (tn > sn) return res;

        // Map<Character, Integer> map = new HashMap<>();

        // for (char c : t.toCharArray()) {
        //     map.put(c, map.getOrDefault(c, 0) + 1);
        // }
        // int counter = map.size();
        // for (int left = 0, right = 0; right < sn; right++) {
        //     char temp = s.charAt(right);

        //     if (map.containsKey(temp)) {
        //         map.put(temp, map.get(temp) - 1);
        //         if (map.get(temp) == 0) counter--;
        //     }

        //     while (counter == 0) {
        //         String newRes = s.substring(left, right+1);

        //         if (res == "") res = newRes;
        //         if (right - left + 1 < res.length()) res = newRes;

        //         char leftC = s.charAt(left++);
        //         if (map.containsKey(leftC)) {
        //             map.put(leftC, map.get(leftC) + 1);
        //             if (map.get(leftC) > 0) counter++;
        //         }
        //         while (left + 1 < sn && !map.containsKey(s.charAt(left))) {
        //             left++;
        //         }
        //     }
        // }
        // return res;
    }
}