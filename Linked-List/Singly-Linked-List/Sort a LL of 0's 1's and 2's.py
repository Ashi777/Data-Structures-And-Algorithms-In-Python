# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or head.next==None: return head
        zeroHead=ListNode(-1); zero=zeroHead
        oneHead=ListNode(-1); one=oneHead
        twoHead=ListNode(-1); two=twoHead
        temp=head
        while temp:
            if temp.val==0:
                zero.next=temp
                zero=temp
            elif temp.val==1:
                one.next=temp
                one=temp
            else:
                two.next=temp
                two=temp
            temp=temp.next
        zero.next=oneHead.next if one else twoHead.next
        one.next=twoHead.next
        two.next=None
        return zeroHead.next

