Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class DSU:
    def __init__(self, n):
        self.rank = [1]*n
        self.parent = [i for i in range(n)]

    def find_upar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_upar(self.parent[node])
        return self.parent[node]
... 
...     def union(self, u, v):
...         ulp_u, ulp_v = self.find_upar(u), self.find_upar(v)
...         if ulp_u == ulp_v:
...             return
...         elif self.rank[ulp_u] < self.rank[ulp_v]:
...             self.parent[ulp_u] = ulp_v
...         elif self.rank[ulp_u] > self.rank[ulp_v]:
...             self.parent[ulp_v] = ulp_u
...         else:
...             self.rank[ulp_u] += 1
...             self.parent[ulp_v] = ulp_u
... 
...     def size(self, node):
...         return self.rank[node]
... 
... 
... class Solution:
...     def removeStones(self, stones: List[List[int]]) -> int:
...         maxRow, maxCol = 0, 0
...         for i, j in stones:
...             maxRow = max(maxRow, i)
...             maxCol = max(maxCol, j)
...         
...         dsu = DSU(maxRow + maxCol + 2)
...         stone_map = {}
...         
...         for i, j in stones:
...             nodeRow, nodeCol = i, j + maxRow + 1
...             dsu.union(nodeRow, nodeCol)
...             stone_map[nodeRow] = 1
...             stone_map[nodeCol] = 1
...         
...         cnt = 0
...         for i in stone_map:
...             if dsu.find_upar(i) == i:
...                 cnt += 1
...         
...         return len(stones) - cnt
