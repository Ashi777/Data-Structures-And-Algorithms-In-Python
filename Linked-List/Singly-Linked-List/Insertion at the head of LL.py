# Definition of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertAtHead(self, head, X):
        new_node = ListNode(X)  # Create a new node with value X
        new_node.next = head    # Point new node's next to the current head
        return new_node         # Return the new node as the new head
