Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
...         dummy = ListNode(-1)
...         dummy.next = head
... 
...         prev = dummy
...         curr = head
... 
...         while curr:
...             
...             while curr.next and curr.val == curr.next.val:
...                 curr = curr.next
... 
...             if prev.next == curr:
...                 prev = prev.next
...           
...             else:
...                 prev.next = curr.next
...             curr = curr.next
...         return dummy.next
