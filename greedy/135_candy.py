class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lres = [1] * n
        rres = [1] * n
        res = []

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                lres[i] = lres[i - 1] + 1
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                rres[j] = rres[j + 1] + 1
        for k in range(n):
            res.append(max(lres[k], rres[k]))
        return sum(res)

        # brute-force, time limit exceeded
        # n = len(ratings)
        # result = [1] * n
        # for i in range(n):
        #     if i + 1 < n:
        #         if ratings[i] > ratings[i + 1] and result[i] == 1:
        #             result[i] += 1
        #             temp = i
        #             while ratings[i] < ratings[i-1] and result[i] >= result[i-1]:
        #                 result[i-1] = result[i] + 1
        #                 i -= 1
        #             i = temp
        #         elif ratings[i] < ratings[i + 1]:
        #             result[i+1] = result[i] + 1
                
        # print(result)
        # return sum(result)


        