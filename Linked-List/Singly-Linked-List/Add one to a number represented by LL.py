# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        carry=self.addHelper(head)
        if carry==1:
            newNode=ListNode(1)
            newNode.next=head
            head=newNode
        return head

    def addHelper(self, temp):
        if temp==None: return 1
        carry=self.addHelper(temp.next)
        temp.val+=carry
        if temp.val<10: return 0
        temp.val=0
        return 1

