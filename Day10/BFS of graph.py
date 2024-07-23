Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #User function Template for python3
... 
... from typing import List
... from queue import Queue
... class Solution:
...     #Function to return Breadth First Traversal of given graph.
...     def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
...         # code here
...         q=[0]
...         ans=[]
...         vis=[0]*V
...         vis[0]=1
...         res=[]
...         while(q):
...             node=q.pop(0)
...             res.append(node)
...             for i in adj[node]:
...                 if not vis[i]:
...                     vis[i]=1
...                     q.append(i)
...         return res
