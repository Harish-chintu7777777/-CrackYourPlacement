Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def allPalindromicPerms(self, s):
...         # code here 
...         def f(i):
...             if i>=n:
...                 res.append(curr.copy())
...                 return
...             for j in range(i, len(s)):
...                 if s[i:j+1] == s[i:j+1][::-1]:
...                     curr.append(s[i:j+1])
...                     f(j+1)
...                     curr.pop()
...                     
...         res, curr = [], []
...         n = len(s)
...         f(0)
...         return res
