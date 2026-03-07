# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        fast=head; slow=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if fast==slow: return self.findLength(fast, slow)
        return 0

    def findLength(self, fast, slow):
        count=1
        fast=fast.next
        while(slow!=fast):
            fast=fast.next
            count+=1
        return count

