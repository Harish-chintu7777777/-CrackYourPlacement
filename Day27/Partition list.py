# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:



        res = []
        curr = head
        while(curr):
            res.append(curr.val)
            curr = curr.next
        l1 = []
        l2 = []
        for i in res:
            if i!=x and i<x:
                l1.append(i)
        for i in res:
            if i not in l1:
                l2.append(i)
        dummy = ListNode(-1)
        cc=dummy
        i=0
        while(i<len(l1)):
            dummy.next=ListNode(l1[i])
            dummy=dummy.next
            i+=1
        i=0
        while(i<len(l2)):
            dummy.next=ListNode(l2[i])
            dummy=dummy.next
            i+=1
        return cc.next

        
