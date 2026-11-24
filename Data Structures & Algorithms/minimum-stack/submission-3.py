class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append({val: val})
            return

        self.stack.append({val: min(val, list(self.stack[-1].values())[0])})

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return list(self.stack[-1].keys())[0] if self.stack else None

    def getMin(self) -> int:
        return list(self.stack[-1].values())[0] if self.stack else None
