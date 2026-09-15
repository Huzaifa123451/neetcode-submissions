class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackMin or val <= self.stackMin[-1]:
            self.stackMin.append(self.stack[-1])
        else:
            self.stackMin.append(self.stackMin[-1])
    
    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
       return self.stackMin[-1]