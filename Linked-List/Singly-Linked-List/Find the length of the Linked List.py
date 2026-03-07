# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        # Your code goes here
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

