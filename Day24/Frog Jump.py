Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def canCross(self, stones: List[int]) -> bool:
... 
...         def f(ind,steps):
...             if ind == n-1:
...                 return True
...             if (ind,steps) in dp:
...                 return dp[(ind,steps)]
...             res = False
...             for j in range(ind+1,n):
...                 if stones[ind] + steps == stones[j]:
...                     res = res or f(j,steps)
...                 if stones[ind] + steps + 1 == stones[j]:
...                     res = res or f(j,steps+1)
...                 if stones[ind] + steps - 1 == stones[j]:
...                     res = res or f(j,steps-1)
...             dp[(ind,steps)] = res
...             return res
...         dp = {}
...         if stones[1] != 1:
...             return False
...         n = len(stones)
