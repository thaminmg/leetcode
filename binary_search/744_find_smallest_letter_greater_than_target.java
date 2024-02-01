class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (letters[mid] > target) {
                right = mid;
            } else if (letters[mid] <= target) {
                left = mid + 1;
            }
        }
        if (letters[left] > target) {
            return letters[left];
        }
        return letters[0];
    }
}