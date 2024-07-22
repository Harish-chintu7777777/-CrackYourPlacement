Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def calculate(self, s: str) -> int:
...         stack = []
...         curr = 0
...         op = "+"
...         if not s:
...             return 0
...         operators = ['+','-','*',"/"]
...         nums = set(str(x) for x in range(10))
...         for i in range(0,len(s)):
...             # print(stack)
...             ch = s[i]
...             if ch in nums:
...                 
...                 curr = curr*10+int(ch)
...             if ch in operators or i == len(s)-1:
...                 # print(op)
...                 if op == '+':
...                     stack.append(curr)
...                 elif op == '-':
...                     stack.append(-curr)
...                 elif op == '/':
...                     stack[-1] = int(stack[-1]/curr)
...                 elif op =="*":
...                     stack[-1] *= curr
... 
...                 curr = 0
...                 op = ch
...                     
