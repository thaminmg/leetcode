class Solution {

    public boolean isOdd(int num) {
        return (num & 1) == 1;
    }

    public boolean threeConsecutiveOdds(int[] arr) {
        int n = arr.length;

        if (n < 3) return false;

        boolean foo = isOdd(arr[0]);
        boolean bar = isOdd(arr[1]);
        boolean foobar = false;
        for (int i = 2; i < n; i++) {
            foobar = isOdd(arr[i]);
            if (foo && bar && foobar) return true;
            if (i != n - 1) {
                foo = bar;
                bar = foobar;
            }  
        }
        return foo && bar && foobar;
    }
}