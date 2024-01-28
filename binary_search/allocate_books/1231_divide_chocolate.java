class Solution {

    private int allocate(int[] sweetness, int limit) {
        int total = 0;
        int count = 0;
        for (int s : sweetness) {
            total += s;
            if (total >= limit) {
                total = 0;
                count++;
            }
        }
        return count;
    }

    public int maximizeSweetness(int[] sweetness, int k) {
        int left = Arrays.stream(sweetness).min().getAsInt();
        int right = Arrays.stream(sweetness).sum() / (k + 1);


        while (left <= right) {
            int mid = left + (right - left) / 2;
            int count = allocate(sweetness, mid);

            if (count >= k + 1) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return right;
    }
}