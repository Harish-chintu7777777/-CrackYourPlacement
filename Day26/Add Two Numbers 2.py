# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def rev(head):
            prev, curr, later = None, head, None
            while(curr):
                later = curr.next
                curr.next = prev
                prev = curr
                curr = later
            return prev
        
        l1, l2 = rev(l1), rev(l2)
        carry, s = 0,0
        head1, head2 = l1, l2
        dummy = ListNode(-1)
        curr = dummy
        while(l1 and l2):
            s = l1.val + l2.val + carry
            curr.next = ListNode(s % 10)
            carry = s // 10
            curr, l1, l2 = curr.next, l1.next, l2.next
        
        while(l1):
            curr.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1, curr = l1.next, curr.next

        while(l2):
            curr.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2, curr = l2.next, curr.next
        while(carry):
            curr.next = ListNode(carry)
            curr = curr.next
            carry -= carry
        return rev(dummy.next)
      

