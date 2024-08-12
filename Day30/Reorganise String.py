Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
...     def reorganizeString(self, s: str) -> str:
...         d=Counter(s)
...         heap=[(-v,k) for k,v in d.items()]
...         heapq.heapify(heap)
...         x1=""
...         while(len(heap)>1):
...             x=heapq.heappop(heap)
...             y=heapq.heappop(heap)
...             x1+=x[1]
...             x1+=y[1]
...             if -x[0]>1:
...                 heapq.heappush(heap,(x[0]+1,x[1]))
...             if -y[0]>1:
...                 heapq.heappush(heap,(y[0]+1,y[1]))
...         if heap:
...             if -heap[0][0]>1:
...                 return ""
...             else:
...                 x1+=heap[0][1]
...         return x1
... 
... 
... 
... 
... 
... 
... 
