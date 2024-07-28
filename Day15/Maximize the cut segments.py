Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... sys.setrecursionlimit(10000)
... 
... class Solution:
...     def maximizeTheCuts(self, n, x, y, z):
...         def f(ind, target):
...             if (ind, target) in dp:
...                 return dp[(ind, target)]
...             if target == 0:
...                 return 0
...             if ind >= len(l):
...                 return -1e9
... 
...             p1 = -1e9
...             if target >= l[ind]:
...                 p1 = 1 + f(ind, target - l[ind])
... 
...             p2 = f(ind + 1, target)
...             
...             dp[(ind, target)] = max(p1, p2)
...             return dp[(ind, target)]
...             
...         l = [x, y, z]
...         l.sort()
...         dp = {}
...         result = f(0, n)
...         return max(result, 0)
