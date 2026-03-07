# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead=ListNode(-1)
        temp=dummyHead
        temp1=l1; temp2=l2
        carry=0
        while temp1!=None or temp2!=None:
            sum1=carry
            if temp1: sum1+=temp1.val
            if temp2: sum1+=temp2.val
            newNode=ListNode(sum1%10)
            carry=sum1//10
            temp.next=newNode
            temp=temp.next
            if temp1: temp1=temp1.next
            if temp2: temp2=temp2.next
        if carry:
            newNode=ListNode(carry)
            temp.next=newNode
        return dummyHead.next

