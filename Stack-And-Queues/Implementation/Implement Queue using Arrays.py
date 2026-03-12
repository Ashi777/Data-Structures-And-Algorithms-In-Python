class ArrayQueue:
    def __init__(self):
        self.first=-1
        self.last=-1
        self.size=1000
        self.queue=[0] * self.size

    def push(self, x):
        if self.last+1>=self.size:
            raise IndexError("Queue overflow")
        if self.first==-1:
            self.first=0
        self.last+=1
        self.queue[self.last]=x

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty queue")
        x = self.queue[self.first]
        if self.first==self.last:
            self.first=-1
            self.last=-1
        else:
            self.first+=1
        return x

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[self.first]

    def isEmpty(self):
        return self.last==-1

