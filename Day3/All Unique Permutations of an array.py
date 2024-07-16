Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def uniquePerms(self, arr, n):
...         def f(arr, l, ds):
...             if len(ds) == n:
...                 res.add(tuple(ds[:]))
...                 return
...             for i in range(n):
...                 if not l[i]:
...                     l[i] = 1
...                     ds.append(arr[i])
...                     f(arr, l, ds)
...                     l[i] = 0
...                     ds.pop()
...                     
...         l = [0] * n
...         ds = []
...         res = set()
...         f(arr, l, ds)
...         res = sorted(res)
...         return res
... 
