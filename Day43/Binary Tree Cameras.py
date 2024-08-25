Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class Solution:
...     def minCameraCover(self, root: Optional[TreeNode]) -> int:
...         
...         def f(root):
...             if not root:
...                 return 1
...             l = f(root.left)
...             r = f(root.right)
... 
...             if l == 0 or r == 0:
...                 cnt[0] += 1
...                 return 2
...             if l == 2 or r == 2:
...                 return 1
... 
...             return 0
... 
...         cnt = [0]
...         x = f(root)
...         if x == 0:
...             cnt[0] += 1
...         
...         return cnt[0]
