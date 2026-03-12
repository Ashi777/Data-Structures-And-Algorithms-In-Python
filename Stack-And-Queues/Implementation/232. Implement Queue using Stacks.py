from queue import LifoQueue
class MyQueue:
    def __init__(self):
        self.S1_input=LifoQueue()
        self.S2_output=LifoQueue()

    def push(self, x: int) -> None:
        self.S1_input.put(x)

    def pop(self) -> int:
        if self.S2_output.empty():
            while not self.S1_input.empty():
                self.S2_output.put(self.S1_input.get())
        x = self.S2_output.get()
        return x

    def peek(self) -> int:
        if self.S2_output.empty():
            while not self.S1_input.empty():
                self.S2_output.put(self.S1_input.get())
        return self.S2_output.queue[-1]

    def empty(self) -> bool:
        return self.S1_input.qsize()==0 and self.S2_output.qsize()==0

