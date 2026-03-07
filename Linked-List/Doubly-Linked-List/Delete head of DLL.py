# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteHead(self, head):
        if head is None:
            return None  # Empty list, nothing to remove

        new_head = head.next  # Step 2
        if new_head:
            new_head.prev = None  # Step 3
        return new_head  # Step 4