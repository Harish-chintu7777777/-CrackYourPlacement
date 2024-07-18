Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def generateParenthesis(self, n: int) -> List[str]:
...         
...         def f(openn,close,s):
...             if len(s) == n*2:
...                 res.append(s)
...                 return 
...             if openn < n:
...                 f(openn+1,close,s+"(")
...             if openn > close:
...                 f(openn,close+1,s+")")
...         res = []
...         f(0,0,"")
