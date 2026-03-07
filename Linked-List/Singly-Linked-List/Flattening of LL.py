# Definiton of singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None, child=None):
#         self.val = val
#         self.next = next
#         self.child = child

class Solution:
    def flattenLinkedList(self, head):
        if head is None or head.next is None: return head
        mergedHead = self.flattenLinkedList(head.next)
        head = self.merge(head, mergedHead)
        return head

    def merge(self, list1, list2):
        dummyNode = ListNode(-1)
        res = dummyNode
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None
        if list1: res.child = list1
        if list2: res.child = list2
        if dummyNode.child: dummyNode.child.next = None
        return dummyNode.child

# TC -> O(2NM)
# SC -> O(N)