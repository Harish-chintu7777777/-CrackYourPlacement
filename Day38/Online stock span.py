Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class StockSpanner:
... 
...     def __init__(self):
...         self.stk = []
... 
...     def next(self, price: int) -> int:
...         span = 1
...         while self.stk and self.stk[-1][0] <= price:
...             span += self.stk.pop()[1]
...         self.stk.append((price, span))
...         return span
