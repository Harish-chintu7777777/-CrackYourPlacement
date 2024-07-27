Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> from typing import List
... 
... class Solution:
...     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
...         
...         def f(ind, zeros, ones):
...             if ind >= len(strs):
...                 return 0
...             if zeros > m or ones > n:
...                 return -1e9
...             if (ind, zeros, ones) in dp:
...                 return dp[(ind, zeros, ones)]
...             
...             o, z = 0, 0
...             for char in strs[ind]:
...                 if char == '0':
...                     z += 1
...                 else:
...                     o += 1
...                     
...             p1 = 0
...             if zeros + z <= m and ones + o <= n:
...                 p1 = 1 + f(ind + 1, zeros + z, ones + o)
...             p2 = f(ind + 1, zeros, ones)
...             dp[(ind, zeros, ones)] = max(p1, p2)
...             return dp[(ind, zeros, ones)]
...         
...         dp = {}
...         return f(0, 0, 0)
