class Solution:
    def maximumTaskPriority(self, n: int, priority: list[int], x: int, y: int) -> int:
        sum = 0
        pi = 0
        count: dict[int, int] = {}
        priority.sort()
        priority.reverse()
        print(priority)
        for i in priority:
            count[i] = 0
    
        for i in range(y):
            if count[priority[pi]] == 0:
                sum += priority[pi]
                count[priority[pi]] = x
                if pi < n - 1:
                    pi += 1
                else: 
                    pi = 0
            
            for key, value in reversed(count.items()):
                if  value != 0:
                    count[key] = value - 1
                    if count[key] == 0:
                        pi = priority.index(key)
            print(count, sum)
        return sum
                
n = 3
priority = [2, 1, 3]
x = 2
y = 3

# n = 3
# priority = [3, 1, 2]
# x = 5
# y = 7
print(Solution().maximumTaskPriority(n, priority, x, y))