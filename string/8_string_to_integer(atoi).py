class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = - 2 ** 31
        MAX = (2 ** 31) - 1
        res = 0
        s = s.strip()
        if s == '' or s == '+' or s == '-': return 0

        flag = False
        if s[0] == '-' or s[0] == '+':
            flag = True if s[0] == '-' else False
            s = s[1:]
        index = 0
        while index < len(s) and s[index] in '0123456789':
            digit = int(s[index])
            res = (res * 10) + digit
            index += 1
        res = - res if flag else res

        if res > MAX: return MAX
        if res < MIN: return MIN
        return res 
        # value, state, pos, sign = 0, 0, 0, 1

        # if len(s) == 0:
        #     return 0

        # while pos < len(s):
        #     current_char = s[pos]
        #     if state == 0:
        #         if current_char == " ":
        #             state = 0
        #         elif current_char == "+" or current_char == "-":
        #             state = 1
        #             sign = 1 if current_char == "+" else -1
        #         elif current_char.isdigit():
        #             state = 2
        #             value = value * 10 + int(current_char)
        #         else:
        #             return 0
        #     elif state == 1:
        #         if current_char.isdigit():
        #             state = 2
        #             value = value * 10 + int(current_char)
        #         else:
        #             return 0
        #     elif state == 2:
        #         if current_char.isdigit():
        #             state = 2
        #             value = value * 10 + int(current_char)
        #         else:
        #             break
        #     else:
        #         return 0
        #     pos += 1

        # value = sign * value
        # value = min(value, 2 ** 31 - 1)
        # value = max(-(2 ** 31), value)

        # return value
 

        
        