Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class Solution:
...     def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
...         if not root:
...             return 0
...         
... 
...         s=0
...         q=[root]
...         while(q):
...             
...             node=q.pop(0)
...             if node:
...                 if node.left and not node.left.left and not node.left.right:
...                         s+= node.left.val
...                 q.append(node.left)
...                 q.append(node.right)
...         return s
...         
... 
... 
