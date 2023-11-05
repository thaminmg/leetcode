class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        if k >= len(arr):
            return max(arr)
        hset = defaultdict()
        res = None

        while True:
            first = arr[0]
            second = arr[1]

            if first > second:
                arr.remove(second)
                arr.append(second)
                if first in hset:
                    hset[first] += 1 
                else:
                    hset[first] = 1
                if hset[first] == k:
                    return first
            else:
                arr.remove(first)
                arr.append(first)
                if second in hset:
                    hset[second] += 1 
                else:
                    hset[second] = 1
                if hset[second] == k:
                    return second
     
        return res
        