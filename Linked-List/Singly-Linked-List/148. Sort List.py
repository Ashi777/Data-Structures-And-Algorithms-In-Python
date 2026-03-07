# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None: return head
        middle=self.findMiddle(head)
        right=middle.next
        left=head
        middle.next=None
        left=self.sortList(left)
        right=self.sortList(right)
        return self.mergeTwoList(left, right)

    def findMiddle(self, head):
        slow=head; fast=head.next   #Fast to be 1 step ahead of slow for edge case
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow

    def mergeTwoList(self, list1, list2):
        dummyNode=ListNode(-1)
        temp=dummyNode
        while(list1!=None and list2!=None):
            if list1.val<list2.val:
                temp.next=list1
                temp=list1
                list1=list1.next
            else:
                temp.next=list2
                temp=list2
                list2=list2.next
        if list1: temp.next=list1
        elif list2: temp.next=list2
        return dummyNode.next

