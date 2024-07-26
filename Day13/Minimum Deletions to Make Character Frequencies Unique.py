Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def minDeletions(self, s: str) -> int:
...         d = Counter(s)
...         val = [j for j in d.values()]
... 
...         val.sort(reverse = True)
...         n = len(val)
...         cnt = 0
...         vis = set()
...         for i in val:
...             if i not in vis:
...                 vis.add(i)
...             else:
...                 while(i in vis):
...                     cnt += 1
...                     i -= 1
...                 if i!=0:
...                     vis.add(i)
...         return cnt
... 
