# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prevLast=None
        while temp!=None:
            KthNode=self.getKthNode(temp, k)
            if not KthNode:
                if prevLast:
                    prevLast.next=temp
                break
            nextNode=KthNode.next
            KthNode.next=None
            self.reverseLL(temp)
            if temp==head:
                head=KthNode
            else:
                prevLast.next=KthNode
            prevLast=temp
            temp=nextNode
        return head

    def reverseLL(self, head):
        temp=head
        prev=None
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev

    def getKthNode(self, temp, k):
        k-=1
        while temp and k>0:
            k-=1
            temp=temp.next
        return temp

# TC -> O(2N)
# SC -> O(1)