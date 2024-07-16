Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Solution:
...     def maxProfit(self, prices: List[int]) -> int:
...         n = len(prices)
...         profit = 0
...         mini = prices[0]
...         for i in range(1,n):
...             if prices[i] - mini > 0:
...                 if prices[i] - mini > profit:
...                     profit = prices[i] - mini
...             else:
...                 mini = min(mini,prices[i])
...         return profit
