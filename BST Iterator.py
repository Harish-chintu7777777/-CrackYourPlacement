Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class BSTIterator:
... 
...     def __init__(self, root: Optional[TreeNode]):
...         self.stack = []
...         while(root):
...             self.stack.append(root)
...             root = root.left
...     def next(self) -> int:
...         res = self.stack.pop()
...         curr = res.right
...         while(curr):
...             self.stack.append(curr)
...             curr = curr.left
...         return res.val
... 
...     def hasNext(self) -> bool:
...         
...         return self.stack != []
... 
... # Your BSTIterator object will be instantiated and called as such:
... # obj = BSTIterator(root)
... # param_1 = obj.next()
