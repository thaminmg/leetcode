class Solution:
    def isPalindrome(self, s: str) -> bool:
        # transform
        transformed_str = ''
        for i in range(len(s)):
            lower_str = s[i].lower()
            if (lower_str >= 'a' and lower_str <= 'z') or (lower_str >= '0' and lower_str <= '9'):
                transformed_str += lower_str
        is_palindrome = True
        for i in range(len(transformed_str) // 2):
            
            if transformed_str[i] != transformed_str[-(i+1)]:
                is_palindrome = False
                break

        return is_palindrome
    
    # str.isalnum()


print(Solution().isPalindrome("0P"))