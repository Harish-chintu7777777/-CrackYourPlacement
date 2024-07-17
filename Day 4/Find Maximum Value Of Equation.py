Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
...         
...         n = len(points)
...         maxi = -1e9
...         heap = []
...         for xj,yj in points:
...             while(heap and xj-heap[0][1] > k):
...                 heapq.heappop(heap)
...             if heap:
...                 maxi = max(maxi,xj+yj - heap[0][0])
...             heapq.heappush(heap,[xj-yj,xj])
...         return maxi
...         
