Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
... 
... 
...         c.sort()
...         res = []
...         def f(l, ind, target):
...             if target == 0:
...                 res.append(l.copy())
...             if target <= 0:
...                 return
...             prev = -1
...             for i in range(ind,len(c)):
...                 if c[i] == prev:
...                     continue
...                 l.append(c[i])
...                 f(l, i+1, target - c[i])
...                 l.pop()
...                 prev = c[i]
...         f([], 0, target)
