import sys

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = min(self.min, x)

    def pop(self) -> None:
        p = self.stack.pop()
        self.min = min(self.stack) if len(self.stack) else sys.maxsize

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()