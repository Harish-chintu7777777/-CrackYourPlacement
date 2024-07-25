Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findPages(self,n ,arr ,m):
...         #code here
...         def f(arr,pages):
...             n = len(arr)
...             students = 1
...             pagesStudent = 0
...             for i in range(n):
...                 if pagesStudent + arr[i] <= pages:
...                     pagesStudent += arr[i]
...                 else:
...                     students += 1
...                     pagesStudent = arr[i]
...             return students
...             
...         if m > n:
...             return -1
...     
...         low = max(arr)
...         high = sum(arr)
...         while low <= high:
...             mid = (low + high) // 2
...             students = f(arr, mid)
...             if students > m:
...                 low = mid + 1
...             else:
...                 high = mid - 1
...         return low
