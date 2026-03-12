class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class LinkedListQueue:
    def __init__(self):
        self.size=0
        self.first=None
        self.last=None

    def push(self, x):
        temp=ListNode(x)
        if self.isEmpty():
            # First element in queue
            self.first = self.last = temp
        else:
            self.last.next = temp
            temp.prev=self.last
            self.last=temp
        self.size+=1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty queue")
        temp=self.first
        if self.first is None:  # Queue became empty
            self.last = None
        else:
            self.first.prev = None
        self.size-=1
        return temp.val

    def peek(self):
        if self.isEmpty():
            raise IndexError("Top from empty queue")
        return self.first.val

    def isEmpty(self):
        return self.size==0

'''
queue = LinkedListQueue()
queue.push(3)
queue.push(7)
print(queue.peek())      # Output: 3
print(queue.pop())      # Output: 3
print(queue.isEmpty())
'''

