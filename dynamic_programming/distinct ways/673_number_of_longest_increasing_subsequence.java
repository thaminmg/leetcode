class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;

        int[] length = new int[n];
        int[] count = new int[n];

        Arrays.fill(length, 1);
        Arrays.fill(count, 1);
        int maxLen = 0, res = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[i]) {
                    if (length[j] + 1 > length[i]) {
                        length[i] = Math.max(length[i], length[j] + 1);
                        count[i] = count[j]; 
                    } else if (length[j] + 1 == length[i]) {
                        count[i] += count[j]; 
                    }
                }
            }
            maxLen = Math.max(maxLen, length[i]);
        }

        for (int i = 0; i < n; i++) {
            if (length[i] == maxLen) {
                res += count[i];
            }
        }
        return res;
    }
}

// Longest increasing subsequence
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        int res = Integer.MIN_VALUE;
        for (int num : dp) {
            res = Math.max(res, num);
        }
        return res;
    }
}