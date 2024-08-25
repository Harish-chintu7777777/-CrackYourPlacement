Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for a binary tree node.
... # class TreeNode:
... #     def __init__(self, val=0, left=None, right=None):
... #         self.val = val
... #         self.left = left
... #         self.right = right
... class Solution:
...     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
... 
...         ans,res = [],[]
... 	    
...         q=deque([(root,0,0)])
... 		
...         while(q):
...             for i in range(len(q)):
...                 node,level,order = q.popleft()
...                 ans.append((order,level,node.val)) 
...                 if node.left: q.append((node.left,level+1,order-1))
...                 if node.right: q.append((node.right,level+1,order+1)) 
... 
...         ans.sort(key = lambda x:(x[0],x[1]))
... 
...         dp = defaultdict(list)
... 
...         for order,level,val in ans: dp[order].append((level,val))
... 
...         for i in dp: 
...             dp[i].sort(key=lambda x:(x[0],x[1])) 
...             res.append([j for k,j in dp[i]])
... 