class Solution:
    def minDeletions(self, s: str) -> int:
        hset = defaultdict(list)
        result = 0
        chars = set()
        count = set()
        for c in s:
            if c in hset:
                hset[c] += 1
            else:
                hset[c] = 1
        for key, value in hset.items():
            if key not in chars and value not in count:
                chars.add(key)
                count.add(value)
            else:
                while value > 0:
                    value -= 1
                    result += 1
                    if key not in chars and value not in count:
                        chars.add(key)
                        count.add(value)
                        break

        return result
                    

                

            
          
        