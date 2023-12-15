class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hset = set()
        lst = []

        for path in paths:
            fromm = path[0]
            too = path[1]
            if too not in hset: 
                lst.append(too)
            if fromm in lst:
                lst.remove(fromm)
            hset.add(fromm)
        return lst[0]
            


                