'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''

class Solution:
    def findPairsWithGivenSum(self, head, target):
        # Your code goes here
        ans=[]
        if not head: return None
        left=head
        right=self.findTail(head)
        while(left.val<right.val):
            if(left.val+right.val==target):
                ans.append([left.val, right.val])
                left=left.next
                right=right.prev
            elif(left.val+right.val<target):
                left=left.next
            else:
                right=right.prev
        return ans

    def findTail(self, head):
        tail=head
        while(tail.next!=None): tail=tail.next
        return tail

