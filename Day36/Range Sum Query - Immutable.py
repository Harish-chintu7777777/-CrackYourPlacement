Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class NumArray:
... 
...     def __init__(self, nums: List[int]):
...         self.prefix=[]
...         cur=0
...         for n in nums:
...             cur+=n
...             self.prefix.append(cur)
...         
... 
...     def sumRange(self, left: int, right: int) -> int:
...         rsum=self.prefix[right]
...         lsum=self.prefix[left-1] if left >0 else 0
