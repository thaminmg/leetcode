class MyQueue:

    def __init__(self):
        self.newestStack = []
        self.oldestStack = []

    def push(self, x: int) -> None:
        self.newestStack.append(x)

    def shiftStacks(self):
        if not self.oldestStack: # if oldStack is empty
            while self.newestStack:
                self.oldestStack.append(self.newestStack.pop())

    def pop(self) -> int:
        self.shiftStacks()
        if self.oldestStack:
            return self.oldestStack.pop()
        else:
            return -1

    def peek(self) -> int:
        self.shiftStacks()
        if self.oldestStack:
            return self.oldestStack[-1]
        else:
            return -1
        
    def empty(self) -> bool:
        return not self.newestStack and not self.oldestStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()