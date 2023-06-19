class Solution:
    def isPalindrome(self, x: int) -> bool:
        # without converting to string
        
        flag = True
        lst = []

        if x < 0:
            flag = False
        else:
            while (x > 0):
                lst.append(x % 10)
                x = int(x / 10)
            lst_len = len(lst)
            if lst_len == 1:
                lst_range = 1
            else:
                lst_range = int(lst_len/2)

            for i in range(lst_range):
                if lst[i] == lst[lst_len-1]:
                    lst_len -= 1
                    continue
                else:
                    flag = False
                    break
        return flag
