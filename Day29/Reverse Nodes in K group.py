# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(head):
            curr, prev = head, None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        n = length // k  
        dummy = ListNode(-1)
        dummy.next = head
        v = dummy

        while n:
            
            v1 = v.next
            curr = v1
            for _ in range(k - 1):
                curr = curr.next
            next_group = curr.next
            curr.next = None

            v.next = rev(v1)

            v1.next = next_group
            v = v1

            n -= 1
        
        return dummy.next
