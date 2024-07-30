Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from typing import List
... 
... class Solution:
...     def findPath(self, mat: List[List[int]]) -> List[str]:
...         def f(i, j, curr, vis):
...             if i == n - 1 and j == n - 1:
...                 l.append(curr)
...                 return
...             
...             vis.add((i, j))  # Add the current cell to the visited set
...             
...             if i + 1 < n and mat[i + 1][j] == 1 and (i + 1, j) not in vis:
...                 f(i + 1, j, curr + 'D', vis)
...             if i - 1 >= 0 and mat[i - 1][j] == 1 and (i - 1, j) not in vis:
...                 f(i - 1, j, curr + 'U', vis)
...             if j + 1 < n and mat[i][j + 1] == 1 and (i, j + 1) not in vis:
...                 f(i, j + 1, curr + 'R', vis)
...             if j - 1 >= 0 and mat[i][j - 1] == 1 and (i, j - 1) not in vis:
...                 f(i, j - 1, curr + 'L', vis)
...             
...             vis.remove((i, j))  # Remove the current cell from the visited set
...         
...         n = len(mat)
...         l, vis = [], set()
...         if mat[0][0] == 0:
...             return []
...         
...         f(0, 0, "", vis)
...         return l
