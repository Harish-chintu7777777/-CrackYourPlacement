Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> """
... # Definition for a Node.
... class Node:
...     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
...         self.val = int(x)
...         self.next = next
...         self.random = random
... """
... 
... class Solution:
...     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
...         d = {None : None}
...         curr = head
...         while(curr):
...             copy = Node(curr.val)
...             d[curr] = copy
...             curr = curr.next
...         curr = head
...         while(curr):
...             copy = d[curr]
...             copy.next = d[curr.next]
...             copy.random = d[curr.random]
...             curr = curr.next
