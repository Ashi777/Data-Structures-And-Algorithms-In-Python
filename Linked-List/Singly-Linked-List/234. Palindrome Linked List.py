# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or head.next==None: return True
        slow=head; fast=head
        while fast.next and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        newHead=self.reverseLL(slow.next)
        first=head
        second=newHead
        while second:
            if first.val!=second.val:
                self.reverseLL(newHead)
                return False
            first=first.next
            second=second.next
        self.reverseLL(newHead)
        return True

    def reverseLL(self, head):
        if not head or head.next==None: return head
        newHead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = deque()
        temp = head
        while temp is not None:
            st.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            if temp.val != st.pop():
                return False
            temp = temp.next
        return True
'''