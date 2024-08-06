class Solution {
    public boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }

    public String reverseVowels(String s) {
        int left = 0, right = s.length() - 1;
        char[] arr = s.toCharArray();

        
        while (left < right) {

            while (left < s.length() && !isVowel(arr[left])) {

                left++;
            }

            while (right >= 0 && !isVowel(arr[right])) {

                right--;
            }

            if (left < right) {
                char temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
        }
        return new String(arr);
    }
}