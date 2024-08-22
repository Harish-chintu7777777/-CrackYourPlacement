Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import defaultdict
... class Solution:
...     def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
...         # Your implementation here
...         adj = defaultdict(list)
...         for i in range(N-1):
...             aa,bb = alien_dict[i], alien_dict[i+1]
...             
...             for j in range(min(len(aa),len(bb))):
...                 if aa[j] != bb[j]:
...                     adj[ord(aa[j]) - 97].append(ord(bb[j]) - 97)
...                     break
...         
...         indeg = [0]*K
...         for i in adj:
...             for it in adj[i]:
...                 indeg[it] += 1
...         q = []
...         for i in range(K):
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
...         for i in range(len(topo)):
...             topo[i] = chr(97+topo[i])
