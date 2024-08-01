Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class Solution:
...     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
...         
...         def is_same_tree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
...             if not s and not t:
...                 return True
...             if not s or not t:
...                 return False
...             if s.val != t.val:
...                 return False
...             return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)
...         
...         def dfs(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
...             if not s:
...                 return False
...             if is_same_tree(s, t):
...                 return True
...             return dfs(s.left, t) or dfs(s.right, t)
...         
...         return dfs(root, subRoot)
