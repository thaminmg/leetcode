class Solution {
    public int countSeniors(String[] details) {
        int res = 0;

        for (String detail : details) {
            int n = detail.length();
            int yearsOld = Integer.parseInt(detail.substring(n - 4, n - 2));

            if (yearsOld > 60) res++;
        }
        return res;
    }
}