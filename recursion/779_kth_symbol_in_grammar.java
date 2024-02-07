class Solution {
    public int helper(int n, int k) {
        if (n == 1) return 0;
        
        int total = (int) Math.pow(2, n - 1);
        int half = total / 2;
        
        if (k > half) {
            return 1 - helper(n - 1, k - half);
        }
        return helper(n - 1, k);
    }
    
    public int kthGrammar(int n, int k) {
        return helper(n, k);
    }
}


// Brute force
// class Solution {
    
//     HashMap<Integer, String> hash = new HashMap();
    
//     public int kthGrammar(int n, int k) {
//         hash.put(1, "0");
        
//         String prev, temp ;
//         for (int i = 2; i <= n; i++) {
//             prev = hash.get(i-1);
//             temp = "";
//             for (int j = 0; j < prev.length(); j++) {
//                 if (prev.charAt(j) == '0') {
//                     temp += "01";
//                 } else {
//                     temp += "10";
//                 }
//             }
//             hash.put(i, temp);
//         }
        
//         return Integer.parseInt(String.valueOf(hash.get(n).charAt(k-1)));
//     }
// }

