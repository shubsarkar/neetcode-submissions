class MinStack:
# the first idea is to use two stacks to maintain the min

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # push the element whichever is smaller current or the prev
        if not self.minStack or val <= self.minStack[-1]: 
            # peek at the last element, we push the val
            self.minStack.append(val)
        else: 
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
