class stackClass:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        if (self.isEmpty()):
            print("Can't peek an empty stack")
        else:
            return self.stack[-1]

    def sizeOf(self):
        return (len(self.stack))

    def isEmpty(self):
        return (self.sizeOf() == 0)
