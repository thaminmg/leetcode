class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0

        for string in bank:
            count = 0
            for ch in string:
                if ch == '1':
                    count += 1
                
            if count > 0:
                res += prev * count
                prev = count
        return res
                    
        