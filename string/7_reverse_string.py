class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        MIN = - pow(2, 31) 
        MAX = pow(2, 31) - 1

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or res == MAX // 10 and digit > MAX % 10) or (res < MIN // 10 or res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit
        return res
    
    new_string = ""
        # flag = False
        
        # minimum = - 2**31
        # maximum = 2**31 - 1
        
        # if x == 0:
        #     return 0
        
        # string = str(x)
        # if string[0] == '-':
        #     string = string[1:]
        #     flag = True
        # while string[-1] == '0':
        #     string = string[0:len(string)-1]
        # for i in range(len(string)):
        #     new_string = string[i] + new_string

        # if flag:
        #     x = - int(new_string)
        # else:
        #     x = int(new_string)
        
        # if x < minimum or x > maximum:
        #     return 0
        # else:
        #     return x
   