# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        temp=head
        while(temp!=None and temp.next!=None):
            nextNode=temp.next
            while(nextNode!=None and nextNode.val==temp.val):
                nextNode=nextNode.next
            temp.next=nextNode
            if nextNode!=None: nextNode.prev=temp
            temp=temp.next
        return head

