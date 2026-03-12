class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class LinkedListStack:
    def __init__(self):
        self.size=0
        self.top_element=None

    def push(self, x):
        temp = ListNode(x)
        temp.next=self.top_element
        self.top_element=temp
        self.size+=1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        temp= self.top_element
        self.top_element=self.top_element.next
        self.size-=1
        return temp.val

    def top(self):
        if self.isEmpty():
            raise IndexError("Top from empty stack")
        return self.top_element.val

    def isEmpty(self):
        return self.size==0

'''
stack = LinkedListStack()
stack.push(3)
stack.push(7)
print(stack.pop())      # Output: 7
print(stack.top())      # Output: 3
print(stack.isEmpty())
'''