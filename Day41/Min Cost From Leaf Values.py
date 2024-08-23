Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def mctFromLeafValues(self, arr: List[int]) -> int:
...         
...         stk = [1e9]
...         n = len(arr)
...         res = 0
...         for i in arr:
...             while(stk and stk[-1] < i ):
...                 top = stk.pop()
...                 res += top*min(stk[-1],i)
...             stk.append(i)
...         
...         while(len(stk) > 2):
...             top = stk.pop()
...             res += top*stk[-1]
...         return res
... 
... 
