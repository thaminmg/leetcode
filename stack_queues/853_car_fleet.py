class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        stack = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort()

        for i in reversed(pairs):
            t = (target - i[0]) /i[1]
            top = stack[-1] if stack else None
            stack.append((i, t))
            if top and t <= top[1]:
                stack.pop()
            

        return len(stack)
        