class Solution {
    public String reverseWords(String s) {
        int n = s.length();
        int right = n - 1;
        char[] res = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        int start = 0, end = 0;
        while (right >= 0) {
            while (right >= 0 && res[right] == ' ') {
                right--;
            }
            end = right + 1;
            while (right >= 0 && res[right] != ' ') {
                right--;
            }
            start = right + 1;
            
            sb.append(s.substring(start, end));
            sb.append(" ");
        }
        
        return sb.toString().trim();
        
        
//         String[] list = s.split(" ");
//         StringBuilder sb = new StringBuilder();
//         for (int i = list.length - 1; i >= 0; i--) {
//             sb.append(list[i]);
//             sb.append(" ");
//         }
        
//         return sb.toString().trim();
    }
}