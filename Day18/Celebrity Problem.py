Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def celebrity(self, mat, n):
...         
...         know_me,I_know = [0]*n, [0]*n
...         for i in range(n):
...             for j in range(n):
...                 if mat[i][j] == 1:
...                     know_me[j] += 1
...                     I_know[i] += 1
...         for i in range(n):
...             if know_me[i] == n-1 and I_know[i] == 0:
...                 return i
...         return -1
