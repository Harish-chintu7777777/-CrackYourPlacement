Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from typing import List

class Solution:
...     def minDifference(self, n: int, arr: List[int]) -> List[List[int]]:
...         ans = []
...         total = sum(arr)
...         dp = set()
... 
...         def solve(ind, sum_val, s1, arr, total, ans, dp):
...             if ind >= len(arr):
...                 return
...             if s1 > len(arr) // 2:
...                 return
...             if s1 == len(arr) // 2:
...                 if sum_val in dp:
...                     return
...                 sum2 = total - sum_val
...                 dp.add(sum_val)
...                 diff = abs(sum_val - sum2)
...                 
...                 if ans:
...                     minSum1 = ans[0][0]
...                     minSum2 = ans[1][0]
...                     min_diff = abs(minSum1 - minSum2)
...                     if diff < min_diff:
...                         ans.clear()
...                         ans.append([sum_val])
...                         ans.append([sum2])
...                 else:
...                     ans.append([sum_val])
...                     ans.append([sum2])
...                 return
...             
...             for i in range(ind, len(arr)):
...                
...                 solve(i + 1, sum_val + arr[i], s1 + 1, arr, total, ans, dp)
...                 
...                 if sum_val not in dp:
...                     solve(i + 1, sum_val, s1, arr, total, ans, dp)
...         
...         solve(0, 0, 0, arr, total, ans, dp)
...         ans.sort()
