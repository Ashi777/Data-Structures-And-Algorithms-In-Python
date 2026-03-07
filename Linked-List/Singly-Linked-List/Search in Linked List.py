# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def searchKey(self, head, key):
        # Your code goes here
        temp=head
        while temp:
            if temp.val==key: return True
            temp=temp.next
        return False