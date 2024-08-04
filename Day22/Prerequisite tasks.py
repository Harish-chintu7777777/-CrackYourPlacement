Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... from collections import defaultdict
... class Solution:
...     def isPossible(self,n,p,pre):
...         #code here
...         adj = defaultdict(list)
...         indeg = [0]*n
...         for i,j in pre:
...             adj[i].append(j)
...             indeg[j] += 1
...         q = []
...         for i in range(n):
...             if indeg[i] == 0:
...                 q.append(i)
...         topo = []
...         while(q):
...             node = q.pop(0)
...             topo.append(node)
...             for it in adj[node]:
...                 indeg[it] -= 1
...                 if indeg[it] == 0:
...                     q.append(it)
...         if len(topo) != n:
...             return False
