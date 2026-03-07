class Solution:
    def reverseDLL(self, head):
        # Your code goes here
        if not head or head.next==None: return head
        prev=None; temp=head
        while temp:
            prev=temp.prev
            temp.prev=temp.next
            temp.next=prev
            temp=temp.prev
        return prev.prev

