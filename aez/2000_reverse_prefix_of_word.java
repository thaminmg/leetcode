class Solution {
    public String reversePrefix(String word, char ch) {
        StringBuilder res = new StringBuilder();
        int cur = 0, i = 0;
        for (; i < word.length(); i++) {
            char temp = word.charAt(i);
            if (temp == ch) {
                res.append(temp);
                res.reverse();
                res.append(word.substring(i+1));
                return res.toString();
            } else {
                res.append(temp);
            }
        }
        return word;
    }
}