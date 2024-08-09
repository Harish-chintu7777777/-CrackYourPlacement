Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for singly-linked list.
... class ListNode:
...     def __init__(self, val=0, next=None):
...         self.val = val
...         self.next = next
... 
... class Solution:
...     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
...         if not head or left == right:
...             return head
... 
...         dummy = ListNode(0)
...         dummy.next = head
...         prev = dummy
... 
...         for i in range(left - 1):
...             prev = prev.next
... 
...         cur = prev.next
...         for i in range(right - left):
...             temp = cur.next
...             cur.next = temp.next
...             temp.next = prev.next
...             prev.next = temp
... 
