# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def insertBeforeHead(self, head, X):
        new_node = ListNode(X)       # Step 1
        new_node.next = head         # Step 2
        if head:                     # Step 3
            head.prev = new_node
        return new_node              # Step 4
    