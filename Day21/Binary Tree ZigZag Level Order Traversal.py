Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class Solution:
...     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
...         q=[]
...         res=[]
...         q.append(root)
...         while q:
...             l=[]
...             for i in range(len(q)):
...                 node=q.pop(0)
...                 if node:
...                     l.append(node.val)
...                     q.append(node.left)
...                     q.append(node.right)
...             if l:
...                 res.append(l)
...         for  i in range(1,len(res),2):
...             res[i]=res[i][::-1]
...         return res
... 
