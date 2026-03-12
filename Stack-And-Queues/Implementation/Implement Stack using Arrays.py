class ArrayStack:
    def __init__(self):
        self.top_index = -1        # renamed to avoid conflict
        self.size = 1000
        self.stack = [0] * self.size

    def push(self, x):
        if self.top_index + 1 >= self.size:
            raise IndexError("Stack overflow")
        self.top_index += 1
        self.stack[self.top_index] = x

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        x = self.stack[self.top_index]
        self.top_index -= 1
        return x

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[self.top_index]

    def isEmpty(self):
        return self.top_index == -1

    