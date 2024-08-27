Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
... # class TreeNode(object):
... #     def __init__(self, x):
... #         self.val = x
... #         self.left = None
... #         self.right = None
... 
... class Codec:
... 
...     def serialize(self, root):
...         res = []
...         def f(root):
...             if not root:
...                 res.append("N")
...                 return 
...             res.append(str(root.val))
...             f(root.left)
...             f(root.right)
...         f(root)  
...         return ",".join(res)
... 
...     def deserialize(self, data):
...         self.i = 0
...         vals = data.split(',')
...         def dfs():
...             if vals[self.i] == 'N':
...                 self.i += 1
...                 return None
...             node = TreeNode(int(vals[self.i]))
...             self.i += 1  
...             node.left = dfs()
...             node.right = dfs()
...             return node
...         return dfs()
... 
... # Your Codec object will be instantiated and called as such:
... # ser = Codec()
... # deser = Codec()
... # ans = deser.deserialize(ser.serialize(root))
