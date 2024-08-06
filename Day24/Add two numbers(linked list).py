# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head =ListNode()
        head=dummy
       
        carry=0
        while((l1 is not None) and (l2 is not None)):
            sum=l1.val+l2.val+carry
            carry=sum//10
            dummy.next=ListNode(sum%10)
            dummy=dummy.next
            l1=l1.next
            l2=l2.next
        while(l1):
            sum=l1.val+carry
            carry=sum//10
            dummy.next=ListNode(sum%10)
            dummy=dummy.next
            l1=l1.next
        while(l2):
            sum=l2.val+carry
            carry=sum//10
            dummy.next=ListNode(sum%10)
            dummy=dummy.next
            l2=l2.next
        if carry:
            dummy.next=ListNode(carry)
        return head.next
        
        
        
       
        
            




