Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> def isPossible(a, b, n, k):
...     a.sort(reverse=True)
...     b.sort()
... 
...     for i in range(n):
...         if (a[i] + b[i] < k):
...             return False
... 
