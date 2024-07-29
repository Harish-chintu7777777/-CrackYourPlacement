Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def equalPartition(self, n, arr):
...         # code here
...         def f(ind,target):
...             if ind >= n:
...                 if target == 0:
...                     return True
...                 return False
...             if target == 0:
...                 return True
...             if (ind,target) in dp:
...                 return dp[(ind,target)]
...             p1 = False
...             if target >= arr[ind]:
...                 p1 = f(ind+1,target-arr[ind])
...             p2 = f(ind+1,target)
...             dp[(ind,target)] = p1 or p2
...             return p1 or p2
...         s = sum(arr)
...         if s%2 != 0:
...             return False
...         dp = {}
