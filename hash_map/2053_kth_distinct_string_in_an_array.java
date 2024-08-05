class Solution {
    public String kthDistinct(String[] arr, int k) {
        Set<String> duplicates = new HashSet<String>();
        Set<String> distincts = new HashSet<String>();

        for (String str : arr) {
            if (duplicates.contains(str)) {
                continue;
            }

            if (distincts.contains(str)) {
                distincts.remove(str);
                duplicates.add(str);
            } else {
                distincts.add(str);
            }
        }
        
        for (String str : arr) {
            if (!duplicates.contains(str)) {
                k--;
            }
            if (k == 0) {
                return str;
            }
        }
        return "";
    }
}