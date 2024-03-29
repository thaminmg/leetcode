class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int sn = s.length();
        int pn = p.length();

        if (pn > sn) return res;

        Map<Character, Integer> map = new HashMap<>();

        for (char c : p.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        int counter = map.size();
        for (int left = 0, right = 0; right < sn; right++) {
            char c = s.charAt(right);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) - 1);
                if (map.get(c) == 0) counter--;
            }

            while (counter == 0) {
                char leftC = s.charAt(left);
                if (map.containsKey(leftC)) {
                    map.put(leftC, map.get(leftC) + 1);
                     if (map.get(leftC) > 0) {
                        counter++;
                    }
                }

                if (right - left + 1 == pn) {
                    res.add(left);
                }
                left++;
            }
        }
        return res;
    }


    // public List<Integer> findAnagrams(String s, String p) {
    //     List<Integer> res = new ArrayList<>();
    //     int sn = s.length();
    //     int pn = p.length();

    //     if (pn > sn) return res;

    //     int left = 0;

    //     for (int right = pn; right <= sn; right++) {
    //         if (isAnagram(s.substring(left, right), p)) {
    //             res.add(left);
    //         }
    //         left++;
    //     }
    //     return res;
    // }

    // public boolean isAnagram(String str1,String str2) {
    //     str1 = str1.replaceAll("\\s", "").toLowerCase();
    //     str2 = str2.replaceAll("\\s", "").toLowerCase();

    //     if (str1.length() != str2.length()) {
    //         return false;
    //     }

    //     char[] charArray1 = str1.toCharArray();
    //     char[] charArray2 = str2.toCharArray();

    //     Arrays.sort(charArray1);
    //     Arrays.sort(charArray2);

    //     return Arrays.equals(charArray1, charArray2);
    // }
}