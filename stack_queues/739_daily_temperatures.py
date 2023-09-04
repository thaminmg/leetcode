class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (temp, index) paris

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append((temperatures[index], index))
        return result

        # n^2, run time limit exceeded
        # result = []
        # stack = []
        # for i in range(len(temperatures)):
        #     stack.append(temperatures[i])

        #     j = i + 1
        #     if j < len(temperatures) and temperatures[j] > temperatures[i]:
        #         result.append(len(stack))
        #     else:
        #         while j < len(temperatures) and temperatures[j] <= temperatures[i]:
        #             stack.append(temperatures[j])
        #             j += 1
        #         if j == len(temperatures):
        #             result.append(0)
        #         else:
        #             result.append(len(stack))
        #     stack.clear()
        # # result.append(0) 
        # return result
        