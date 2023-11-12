class Solution:

    def countAndSay(self, n: int) -> str:

        def helper(string):
            if string == '': return '1'

            res = ''
            length = len(string)
            count = 1
            char = string[0]
            for i in range(len(string)-1):
                if string[i] != string[i + 1]:
                    res += f'{count}{char}'
                    count = 1
                    char = string[i+1]
                else:
                    count += 1
            res += f'{count}{char}'
            return res
                
        res = ''
        for i in range(1, n+1):
            res = helper(res)
        return res
        
        