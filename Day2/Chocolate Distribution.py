Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... class Solution:
... 
...     def findMinDiff(self, A,N,M):
... 
...         # code here
...         A.sort()
...         diff = float('inf')
...         for i in range(len(A)-M+1):
...             x = A[M+i-1]-A[i]
...             if x<diff:
...                 diff = x
...         return diff
