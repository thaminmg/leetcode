class Solution:
    def reverse(self, x: int) -> int:
        new_string = ""
        flag = False
        
        minimum = - 2**31
        maximum = 2**31 - 1
        
        if x == 0:
            return 0
        
        string = str(x)
        if string[0] == '-':
            string = string[1:]
            flag = True
        if string[-1] == '0':
            string = string[0:len(string)-1]
        for i in range(len(string)):
            new_string = string[i] + new_string

        if flag:
            x = - int(new_string)
        else:
            x = int(new_string)
        
        if x < minimum or x > maximum:
            return 0
        else:
            return x
