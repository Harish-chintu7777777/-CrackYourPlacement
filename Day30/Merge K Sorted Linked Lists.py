Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
... #         self.val = val
... #         self.next = next
... 
... class Solution:
...     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
... 
...         def merge(left, right):
...             dummy = ListNode(-1)
...             curr = dummy
...             
...             while left and right:
...                 if left.val <= right.val:
...                     curr.next = left
...                     left = left.next
...                 else:
...                     curr.next = right
...                     right = right.next
...                 curr = curr.next
... 
...             if left:
...                 curr.next = left
...             if right:
...                 curr.next = right
... 
...             return dummy.next
... 
...         def divide(lists):
...             if not lists:
...                 return None
...             if len(lists) == 1:
...                 return lists[0]
...             
...             mid = len(lists) // 2
...             left = divide(lists[:mid])
...             right = divide(lists[mid:])
...             return merge(left, right)
... 
...         return divide(lists)
