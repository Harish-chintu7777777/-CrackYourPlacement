Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def countArrangement(self, n: int) -> int:
...         
...         def f(ind, temp):
...             if len(temp) == n:
...                 cnt[0] += 1
...                 return
...             for i in range(1,n+1):
...                 if i not in temp and (ind % i == 0 or i % ind == 0):
... 
...                     temp.append(i)
...                     f(ind + 1, temp)
...                     temp.pop()
...                     
...         cnt = [0]
...         f(1, [])
