from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()
        self.size=0

    def push(self, x: int) -> None:
        s=self.q.qsize()
        self.q.put(x)
        self.size+=1
        for i in range(s):
            self.q.put(self.q.get())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Pop in empty stack")
        self.size-=1
        return self.q.get()

    def top(self) -> int:
        if self.empty():
            raise IndexError("Top from empty stack")
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.size==0
