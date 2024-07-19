Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
... class Solution:
...     def Anagrams(self, words, n):
...         d = {}
...         for i in words:
...             v = "".join(sorted(i))
...             if v not in d:
...                 d[v] = [i]
...             else:
...                 d[v] += [i]
... 
...         res = []
...         for i in d:
...             res.append(d[i])
