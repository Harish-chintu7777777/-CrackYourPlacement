Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
...         
...         heap = []
...         n = len(heights)
...         for i in range(n-1):
...             d = heights[i+1] - heights[i]
...             if d <= 0:
...                 continue
...             bricks -= d
...             heapq.heappush(heap,-d)
...             if bricks < 0:
...                 ladders -= 1
...                 bricks += -1*heapq.heappop(heap)
...             if ladders < 0:
...                 return i
...         return len(heights) - 1
... 
