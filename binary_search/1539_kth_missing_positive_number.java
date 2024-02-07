class Solution {
    public int findKthPositive(int[] arr, int k) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] - mid - 1 < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left + k;
    }
}


// Brute force
// class Solution {
//     public int findKthPositive(int[] arr, int k) {
//         if (k <= arr[0] - 1) {
//             return k;
//         }
//         k -= arr[0] - 1;

//         int n = arr.length;
//         for (int i = 0; i < n - 1; i++) {
//             int diff = arr[i+1] - arr[i] - 1;

//             if (k <= diff) {
//                 return arr[i] + k;
//             }
//             k -= diff;
//         }
//         return arr[n - 1] + k;
//     }
// }