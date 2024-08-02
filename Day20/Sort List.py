# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        curr=head
        while(curr):
            l.append(curr.val)
            curr=curr.next
        l.sort()
        hari=ListNode(-1)
        indu=hari
        for i in l:
            hari.next=ListNode(i)
            hari=hari.next
        return indu.next
