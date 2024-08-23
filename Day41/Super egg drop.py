Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def dfs(f, remain):
...             if remain == 0:
...                 return 0
... 
...             if remain == 1:
...                 return f
... 
...             if f == 0:
...                 return 0
... 
...             if f == 1:
...                 return 1
... 
...             if (f, remain) in memo:
...                 return memo[(f, remain)]
... 
...             res = float('inf')
...             lo, hi = 0, f
... 
...             while lo <= hi:
...                 mid = (lo + hi) // 2
... 
...                 breaks = 1 + dfs(mid - 1, remain - 1)
...                 not_breaks = 1 + dfs(f - mid, remain)
... 
...                 worst = max(breaks, not_breaks)
...                 res = min(res, worst)
... 
...                 if breaks <= not_breaks:
...                     lo = mid + 1
...                 else:
...                     hi = mid - 1
... 
...             memo[(f, remain)] = res
... 
...             return memo[(f, remain)]
... 
...         memo = dict()
... 
...         return dfs(n, k)
