class Solution:
    def romanToInt(self, s: str) -> int:
        konstant = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        
        str_len = len(s)
        lst = []
        total = 0

        for i in range(str_len):
            lst.append(s[i])

        for i in range(len(lst)):
            if (i != len(lst) - 1):
                if ((lst[i] == "I" and (lst[i+1] == "V" or lst[i+1] == "X")) or 
                (lst[i] == "X" and (lst[i+1] == "L" or lst[i+1] == "C")) or 
                (lst[i] == "C" and (lst[i+1] == "D" or lst[i+1] == "M"))):
                    total -= konstant[lst[i]]
                    continue
            total += konstant[lst[i]]

        return total
