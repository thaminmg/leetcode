class Solution {
    public int passThePillow(int n, int time) {
        int rounds = time / (n - 1);
        int extra = time % (n - 1);

        if ((rounds & 1) == 1) {
            return n - extra;
        } else {
            return extra + 1;
        }

    }
}