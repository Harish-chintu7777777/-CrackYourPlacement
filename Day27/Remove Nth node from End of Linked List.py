# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        c=0
        while(curr):
            c+=1
            curr=curr.next
        if c==1:
            return None
        curr=head
        t=c-n
        if t==0:
            curr=curr.next
            head=None
            head=curr
            return head
       
        while(t-1>0):
            curr=curr.next
            t-=1
        curr.next=curr.next.next
        return head
        
        

