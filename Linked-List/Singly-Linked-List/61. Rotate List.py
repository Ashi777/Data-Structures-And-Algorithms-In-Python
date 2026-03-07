# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0: return head
        length=1; tail=head
        while tail.next!=None:
            tail=tail.next
            length+=1
        if (k%length==0): return head
        k=k%length
        tail.next=head
        newLastNode=self.findNthNode(head, length-k)
        head=newLastNode.next
        newLastNode.next=None
        return head

    def findNthNode(self, temp, k):
        count=1
        while temp:
            if count==k: return temp
            count+=1
            temp=temp.next
        return temp

# TC -> O(2NM)
# SC -> O(N)