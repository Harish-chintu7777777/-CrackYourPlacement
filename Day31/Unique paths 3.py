Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from typing import List
... 
... class Solution:
...     def uniquePathsIII(self, grid: List[List[int]]) -> int:
... 
...         def f(sx, sy, dx, dy, z_c, vis):
...             if sx == dx and sy == dy:
...                 return 1 if z_c == 0 else 0
...             
...             paths = 0
...             for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
...                 nrow, ncol = i + sx, j + sy 
...                 if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] != -1 and (nrow, ncol) not in vis:
...                     vis.add((nrow, ncol))
...                     paths += f(nrow, ncol, dx, dy, z_c - 1, vis)
...                     vis.remove((nrow, ncol)) 
...             
...             return paths
... 
...         sx, sy = -1, -1
...         dx, dy = -1, -1 
...         z_c = 1  
...         m, n = len(grid), len(grid[0])
...         
...         for i in range(m):
...             for j in range(n):
...                 if grid[i][j] == 1:
...                     sx, sy = i, j
...                 if grid[i][j] == 2:
...                     dx, dy = i, j
...                 if grid[i][j] == 0:
...                     z_c += 1
...         
...         vis = set()
...         vis.add((sx, sy))
...         return f(sx, sy, dx, dy, z_c, vis)
