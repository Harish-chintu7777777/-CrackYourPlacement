
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
