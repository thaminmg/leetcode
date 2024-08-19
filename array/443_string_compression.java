class Solution {
    public int compress(char[] chars) {
        int res = 0, i = 0;
        while (i < chars.length) {
            int count = 1;
            while (i + count < chars.length && chars[i + count] == chars[i]) {
                count++;
            }
            chars[res++] = chars[i];
            if (count > 1) {
                for (char c : Integer.toString(count).toCharArray()) {
                    chars[res++] = c;
                }
            }
            i += count;
        }
        return res;
    }
}