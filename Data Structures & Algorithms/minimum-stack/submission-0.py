class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        return self.stack
        

    def pop(self) -> None:
        self.stack.pop()
        return self.stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        a = sorted(self.stack)
        return a[0]
        
