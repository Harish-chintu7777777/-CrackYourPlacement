Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkReverse(arr, n):
...     ind1,ind2 = -1,-1
...     f = 0
...     for i in range(n-1):
...         if arr[i] > arr[i+1]:
...             if ind1 == -1:
...                 ind1 = i
...             ind2 = i+1
...     arr = arr[:ind1] + arr[ind1:ind2+1][::-1] + arr[ind2+1:]
...     print(arr)
...     for i in range(n-1):
...         if arr[i] > arr[i+1]:
...             return False
...     return True
